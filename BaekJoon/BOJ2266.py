from sys import stdin

N,K = map(int,stdin.readline().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1,N+1):
    dp[1][i] = i
for i in range(1,K+1):
    dp[i][1] = 1

for i in range(2,K+1):
    for j in range(2,N+1):
        dp[i][j] = float("inf")

        for k in range(1,j+1):
            dp[i][j] = min(dp[i][j],max(dp[i-1][k-1],dp[i][j-k])+1)

print(dp[K][N])