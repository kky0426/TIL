from sys import stdin

N = int(stdin.readline())

dp = [float("inf")]*100001
dp[2] = dp[5] = 1

for i in range(3,N+1):
    dp[i] = min(dp[i],dp[i-2]+1,dp[i-5]+1)


print(dp[:N+1])