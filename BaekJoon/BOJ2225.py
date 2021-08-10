from sys import stdin

N,K = map(int,stdin.readline().split())

dp=[[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0]=1


for i in range(1,K+1):
    for j in range(N+1):
        dp[j][i] = (dp[j-1][i]+dp[j][i-1])%1000000000

print(dp[-1][-1])
