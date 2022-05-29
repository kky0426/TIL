from sys import stdin

N,Q = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))
tree = [0]*(4*N)

def init(left,right,node):
    if left == right:
        tree[node] = nums[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left,mid,node*2)+init(mid+1,right,node*2+1)
    return tree[node]

def query(left,right,node,qLeft,qRight):
    if qLeft>right or left>qRight:
        return 0

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    return query(left,mid,node*2,qLeft,qRight) + query(mid+1,right,node*2+1,qLeft,qRight)

def update(left,right,node,idx,diff):
    if idx<left or idx>right:
        return
    tree[node]+=diff
    if left!=right:
        mid = (left+right)//2
        update(left,mid,node*2,idx,diff)
        update(mid+1,right,node*2+1,idx,diff)

init(0,N-1,1)
for _ in range(Q):
    x,y,a,b = map(int,stdin.readline().split())
    if y<x:
        x,y = y,x
    print(query(0,N-1,1,x-1,y-1))
    diff = b-nums[a-1]
    nums[a-1] = b
    update(0,N-1,1,a-1,diff)