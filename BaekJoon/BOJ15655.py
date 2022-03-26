from sys import stdin

N,M = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))
nums.sort()
ans = []
def dfs(idx,depth):
    if depth == M:
        print(*ans)
        return

    for i in range(idx+1,len(nums)):
        ans.append(nums[i])
        dfs(i,depth+1)
        ans.pop()

dfs(-1,0)
