from sys import stdin

N,M = map(int,stdin.readline().split())
tree = [0]*(4*N)
nums = [int(stdin.readline()) for _ in range(N)]

def init(left,right,node):
    if left == right:
        tree[node] = nums[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = min(init(left,mid,node*2),init(mid+1,right,node*2+1))
    return tree[node]

def query(left,right,node,qLeft,qRight):
    if qLeft>right or qRight<left:
        return float("inf")

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    return min(query(left,mid,node*2,qLeft,qRight),query(mid+1,right,node*2+1,qLeft,qRight))

init(0,N-1,1)
for _ in range(M):
    s,e = map(int,stdin.readline().split())
    print(query(0,N-1,1,s-1,e-1))