from sys import stdin

N,M,K = map(int,stdin.readline().split())

nums = [int(stdin.readline()) for _ in range(N)]
tree = [0]*(4*N)
lazy = [0]*(4*N)

def init(left,right,node):
    if left == right:
        tree[node] = nums[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left,mid,node*2)+init(mid+1,right,node*2+1)
    return tree[node]

def query(left,right,node,qLeft,qRight):
    update_lazy(left,right,node)
    if qLeft>right or left>qRight:
        return 0

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    return query(left,mid,node*2,qLeft,qRight)+query(mid+1,right,node*2+1,qLeft,qRight)

def update_lazy(left,right,node):
    if lazy[node]!=0:
        tree[node]+=(right-left+1)*lazy[node]
        if left != right:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0

def update_range(left,right,node,uLeft,uRight,val):
    update_lazy(left,right,node)

    if uRight<left or right<uLeft:
        return

    if uLeft<=left and right<=uRight:
        tree[node]+=(right-left+1)*val
        if left!=right:
            lazy[node*2]+=val
            lazy[node*2+1]+=val
        return

    mid = (left+right)//2
    update_range(left,mid,node*2,uLeft,uRight,val)
    update_range(mid+1,right,node*2+1,uLeft,uRight,val)
    tree[node] = tree[node*2]+tree[node*2+1]


init(0,N-1,1)
for _ in range(M+K):
    line = list(map(int,stdin.readline().split()))
    if line[0] == 1:
        a,b,c,d = line
        update_range(0,N-1,1,b-1,c-1,d)
    else:
        a,b,c = line
        print(query(0,N-1,1,b-1,c-1))