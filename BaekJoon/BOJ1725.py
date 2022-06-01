from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(N)]
tree = [0]*(4*N)

def init(left,right,node):
    if left == right:
        tree[node] = left
        return tree[node]

    mid = (left+right)//2
    l_idx = init(left,mid,node*2)
    r_idx = init(mid+1,right,node*2+1)
    if nums[l_idx]>nums[r_idx]:
        tree[node] = r_idx
    else:
        tree[node] = l_idx
    return tree[node]

def query(left,right,node,qLeft,qRight):
    if qLeft>right or qRight<left:
        return -1

    if qLeft<=left and right<=qRight:
        return tree[node]

    mid = (left+right)//2
    l_idx = query(left,mid,node*2,qLeft,qRight)
    r_idx = query(mid+1,right,node*2+1,qLeft,qRight)

    if l_idx == -1:
        return r_idx
    elif r_idx == -1:
        return l_idx
    else:
        if nums[l_idx] > nums[r_idx]:
            return r_idx
        else:
            return l_idx


def solve(left,right):
    idx = query(0,N-1,1,left,right)
    s = (right-left+1)*nums[idx]

    if left<=idx-1:
        temp = solve(left,idx-1)
        s = max(s,temp)

    if idx+1<=right:
        temp = solve(idx+1,right)
        s = max(s,temp)

    return s
init(0,N-1,1)
print(solve(0,N-1))