from sys import stdin

N = int(stdin.readline())

dp = [0]*(N+1)

dp[1] = 1
if N>1:
    dp[2] = 1
if N>2:
    dp[3] = 2
for i in range(4,N+1):
    dp[i] = (dp[i-1]+dp[i-3])%1000000009

print(dp[N])
