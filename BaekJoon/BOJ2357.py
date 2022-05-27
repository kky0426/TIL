from sys import stdin

N,M = map(int,stdin.readline().split())

nums = [int(stdin.readline()) for _ in range(N)]

min_tree = [0]*(4*N)
max_tree = [0]*(4*N)

def min_init(left,right,node):
    if left == right:
        min_tree[node] = nums[left]
        return min_tree[node]
    mid = (left+right)//2
    min_tree[node] = min(min_init(left,mid,node*2),min_init(mid+1,right,node*2+1))
    return min_tree[node]

def min_query(left,right,node,qLeft,qRight):
    if qRight<left or right<qLeft:
        return float("inf")

    if qLeft<=left and right<=qRight:
        return min_tree[node]

    mid = (left+right)//2
    return min(min_query(left,mid,node*2,qLeft,qRight),min_query(mid+1,right,node*2+1,qLeft,qRight))

def max_init(left,right,node):
    if left == right:
        max_tree[node] = nums[left]
        return max_tree[node]
    mid = (left+right)//2
    max_tree[node] = max(max_init(left,mid,node*2),max_init(mid+1,right,node*2+1))
    return max_tree[node]

def max_query(left,right,node,qLeft,qRight):
    if qRight<left or right<qLeft:
        return 0
    if qLeft<=left and right<=qRight:
        return max_tree[node]

    mid = (left+right)//2
    return max(max_query(left,mid,node*2,qLeft,qRight),max_query(mid+1,right,node*2+1,qLeft,qRight))


min_init(0,N-1,1)
max_init(0,N-1,1)

for _ in range(M):
    a,b = map(int,stdin.readline().split())
    print(min_query(0,N-1,1,a-1,b-1),max_query(0,N-1,1,a-1,b-1))

