from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
tree= [0]*(4*N)

def init(left,ringt,node):
    if left == ringt:
        tree[node] = nums[left]
        return tree[node]

    mid = (left+ringt)//2
    tree[node] = min(init(left,mid,node*2),init(mid+1,ringt,node*2+1))
    return tree[node]

def query(left,right,node,qLeft,qRgiht):
    if qLeft>right or qRgiht<left:
        return float("inf")

    if qLeft<=left and right<=qRgiht:
        return tree[node]

    mid = (left+right)//2
    return min(query(left,mid,node*2,qLeft,qRgiht),query(mid+1,right,node*2+1,qLeft,qRgiht))

def update(left,right,node,idx,val):
    if idx<left or idx>right:
        return tree[node]

    if left == right:
        tree[node] = val
        return tree[node]

    mid = (left+right)//2
    tree[node] = min(update(left,mid,node*2,idx,val),update(mid+1,right,node*2+1,idx,val))
    return tree[node]

init(0,N-1,1)
M = int(stdin.readline())
for _ in range(M):
    cmd,i,j = map(int,stdin.readline().split())
    if cmd == 1:
        nums[i-1] = j
        update(0,N-1,1,i-1,j)
    else:
        print(query(0,N-1,1,i-1,j-1))
