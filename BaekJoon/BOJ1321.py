from sys import stdin

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
tree = [0]*(4*N)

def init(left,right,node):
    if left == right:
        tree[node] = nums[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = init(left,mid,node*2)+init(mid+1,right,node*2+1)
    return tree[node]

def update(left,right,node,idx,val):
    if idx<left or idx>right:
        return
    tree[node]+=val
    if left!=right:
        mid = (left+right)//2
        update(left,mid,node*2,idx,val)
        update(mid+1,right,node*2+1,idx,val)

def query(left,right,node,val):
    if left == right:
        return left
    mid = (left+right)//2

    if tree[node*2]>=val:
        return query(left,mid,node*2,val)
    else:
        return query(mid+1,right,node*2+1,val-tree[node*2])

M = int(stdin.readline())
init(0,N-1,1)
for _ in range(M):
    line = list(map(int,stdin.readline().split()))
    if len(line) == 3:
        _,i,a = line
        nums[i-1]+=a
        update(0,N-1,1,i-1,a)
    else:
        _,i = line
        print(query(0,N-1,1,i)+1)


