from sys import stdin

N,M = map(int,stdin.readline().split())

fuel = [list(map(int,stdin.readline().split())) for _ in range(N)]

INF = float("inf")
dp = [[[INF,INF,INF] for _ in range(M)] for _ in range(N)]

for i in range(M):
    dp[0][i][0] = fuel[0][i]
    dp[0][i][1] = fuel[0][i]
    dp[0][i][2] = fuel[0][i]

for i in range(1,N):
    for j in range(M):
        if j == 0:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2])+fuel[i][j]
            dp[i][j][1] = dp[i-1][j][0]+fuel[i][j]
        elif j == M-1:
            dp[i][j][1] = dp[i-1][j][2]+fuel[i][j]
            dp[i][j][2] = min(dp[i-1][j-1][0],dp[i-1][j-1][1])+fuel[i][j]
        else:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2])+fuel[i][j]
            dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2])+fuel[i][j]
            dp[i][j][2] = min(dp[i-1][j-1][0],dp[i-1][j-1][1])+fuel[i][j]

ans = INF
for i in range(M):
    ans = min(min(dp[-1][i]),ans)

print(ans)