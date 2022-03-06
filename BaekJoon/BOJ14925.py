from sys import stdin

N,M = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    if grid[i][0] == 0:
        dp[i][0] = 1

for j in range(M):
    if grid[0][j] == 0:
        dp[0][j] = 1
        
for i in range(1,N):
    for j in range(1,M):
        if grid[i][j] == 0:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1

ans = 0
for arr in dp:
    ans = max(ans,max(arr))
print(ans)
