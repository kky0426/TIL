from sys import stdin

N,M,K = map(int,stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(N)]
tree = [0]*(4*N)

def init(start,end,node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start,mid,node*2)+init(mid+1,end,node*2+1)
    return tree[node]

def query(start,end,node,left,right):
    if left>end or right<start:
        return 0

    if left<=start and end<=right:
        return tree[node]

    mid = (start+end)//2
    return query(start,mid,node*2,left,right)+query(mid+1,end,node*2+1,left,right)

def update(start,end,node,idx,diff):
    if idx<start or idx>end:
        return
    tree[node]+=diff
    if start!=end:
        mid = (start+end)//2
        update(start,mid,node*2,idx,diff)
        update(mid+1,end,node*2+1,idx,diff)

init(0,N-1,1)
for _ in range(M+K):
    a,b,c = map(int,stdin.readline().split())
    if a == 1:
        diff = c-nums[b-1]
        nums[b-1] = c
        update(0,N-1,1,b-1,diff)
    else:
        print(query(0,N-1,1,b-1,c-1))