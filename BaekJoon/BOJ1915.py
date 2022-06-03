from sys import stdin

N,M = map(int,stdin.readline().split())
grid = [list(stdin.readline().rstrip()) for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if grid[i-1][j-1] == '1':
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

ans = 0
for arr in dp:
    ans = max(ans,max(arr))
print(ans**2)