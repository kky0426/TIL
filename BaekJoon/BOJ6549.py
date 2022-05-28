from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def init(left,right,node):
    if left == right:
        tree[node] = left
        return tree[node]
    mid = (left+right)//2
    left_idx = init(left,mid,node*2)
    right_idx = init(mid+1,right,node*2+1)
    if nums[left_idx]>nums[right_idx]:
        tree[node] = right_idx
    else:
        tree[node] = left_idx
    return tree[node]

def query(left,right,node,qLeft,qRight):
    if qRight<left or right<qLeft:
        return -1

    if qLeft<=left and right<=qRight:
        return tree[node]
    mid = (left+right)//2
    left_idx = query(left,mid,node*2,qLeft,qRight)
    right_idx = query(mid+1,right,node*2+1,qLeft,qRight)

    if left_idx == -1:
        return right_idx
    elif right_idx == -1:
        return left_idx
    else:
        if nums[left_idx]>nums[right_idx]:
            return right_idx
        else:
            return left_idx

def get_max(left,right):
    idx = query(0,N-1,1,left,right)
    s = (right-left+1)*nums[idx]

    if left<=idx-1:
        temp = get_max(left,idx-1)
        s = max(s,temp)
    if right>=idx+1:
        temp = get_max(idx+1,right)
        s = max(s,temp)
    return s

while True:
    nums = list(map(int,stdin.readline().split()))
    if nums[0] == 0:
        break
    nums = nums[1:]
    N = len(nums)
    tree = [0]*(4*N)
    init(0,N-1,1)
    ans = get_max(0,N-1)
    print(ans)
