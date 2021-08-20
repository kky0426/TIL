from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def dfs(nums):
    if len(temp) == 6:
        ans.append(temp[:])
        return
    if not nums:
        return

    for i in range(len(nums)):
        temp.append(nums[i])
        dfs(nums[i+1:])
        temp.pop()


while True:
    ans = []
    line = list(map(int,stdin.readline().split()))
    if line[0] == 0:
        break
    N = line[0]
    nums = line[1:]
    temp=[]
    dfs(nums)

    for i in ans:
        for j in i:
            print(j,end=" ")
        print()
    print()
