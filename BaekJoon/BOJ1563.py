from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N = int(stdin.readline())

dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N)]

def dfs(day,late,absent):
    if late == 2 or absent == 3:
        return 0

    if day == N:
        return 1

    if dp[day][late][absent] == -1:
        dp[day][late][absent] = dfs(day+1,late,0) + dfs(day+1,late+1,0)+dfs(day+1,late,absent+1)

    return dp[day][late][absent]

print(dfs(0,0,0)%1000000)
