from sys import stdin

N,M = map(int,stdin.readline().split())

book = [0]+[list(map(int,stdin.readline().split())) for _ in range(M)]

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if j-book[i][0]>=0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-book[i][0]]+book[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[M][N])
