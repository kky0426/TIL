from sys import stdin
import sys
sys.setrecursionlimit(10**5)
N = int(stdin.readline())

mine = [int(stdin.readline()) for _ in range(N)]
ans = []
def max_idx(left,right):
    idx = left
    val = mine[left]
    for i in range(left+1,right+1):
        if mine[i]>val:
            idx = i
            val = mine[i]
    return idx

def boom(left,right):
    point = max_idx(left,right)
    global ans
    ans.append(point)
    cur_l = point
    cur_r = point

    while cur_l>left:
        if mine[cur_l]>mine[cur_l-1]:
            cur_l-=1
        else:
            break

    while cur_r<right:
        if mine[cur_r]>mine[cur_r+1]:
            cur_r+=1
        else:
            break

    if cur_l>left: boom(left,cur_l-1)
    if cur_r<right: boom(cur_r+1,right)

boom(0,N-1)
ans.sort()
for n in ans:
    print(n+1)
