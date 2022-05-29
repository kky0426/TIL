from sys import stdin

N,M,K= map(int, stdin.readline().split())

nums = [int(stdin.readline()) for _ in range(N)]
tree = [0]*(4*N)
mod = 1000000007

def init(left,right,node):
    if left == right:
        tree[node] = nums[left]
        return tree[node]

    mid = (left+right)//2
    tree[node] = ((init(left,mid,node*2)%mod)*(init(mid+1,right,node*2+1)%mod))%mod
    return tree[node]

def query(left,right,node,qLeft,qRight):
    if qLeft>right or left>qRight:
        return 1

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    return ((query(left,mid,node*2,qLeft,qRight)%mod)*(query(mid+1,right,node*2+1,qLeft,qRight)%mod))%mod

def update(left,right,node,idx,val):
    if idx<left or idx>right:
        return tree[node]
    if left == right:
        tree[node] = val
        return tree[node]
    mid = (left+right)//2
    tree[node] = ((update(left,mid,node*2,idx,val)%mod)*(update(mid+1,right,node*2+1,idx,val)%mod))%mod
    return tree[node]

init(0,N-1,1)

for _ in range(M+K):
    a,b,c = map(int,stdin.readline().split())
    if a == 1:
        nums[b-1] = c
        update(0,N-1,1,b-1,c)
    else:
        print(query(0,N-1,1,b-1,c-1)%mod)