from sys import stdin

N = int(stdin.readline())

dp = [i for i in range(N+1)]

for i in range(7,N+1):
    dp[i] = max(dp[i-3]*2,dp[i-4]*3,dp[i-5]*4)

print(dp[N])
