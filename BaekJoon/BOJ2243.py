from sys import stdin

N = int(stdin.readline())
MAX = 1000001
tree = [0]*(4*MAX)

def query(left,right,node,count):
    if left == right:
        return left

    mid = (left+right)//2
    if tree[node*2]>=count:
        return query(left,mid,node*2,count)
    else:
        return query(mid+1,right,node*2+1,count-tree[node*2])

def update(left,right,node,idx,diff):
    if idx>right or idx<left:
        return
    tree[node]+=diff
    mid = (left+right)//2
    if left!=right:
        update(left,mid,node*2,idx,diff)
        update(mid+1,right,node*2+1,idx,diff)

for _ in range(N):
    line = list(map(int,stdin.readline().split()))
    if line[0] == 1:
        a,b = line
        idx = query(0,MAX-1,1,b)
        print(idx)
        update(0,MAX-1,1,idx,-1)
    else:
        a,b,c = line
        update(0,MAX-1,1,b,c)