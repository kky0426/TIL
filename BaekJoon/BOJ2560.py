from sys import stdin

a,b,d,N = map(int,stdin.readline().split())

dp = [0]*(N+1)

for i in range(a):
    dp[i] = 1

for i in range(a,N+1):
    if i>=b:
        dp[i] = (dp[i-1]+dp[i-a]-dp[i-b])%1000
    else:
        dp[i] = (dp[i-1]+dp[i-a])%1000


if N>=d:
    print((dp[N]-dp[N-d])%1000)
else:
    print(dp[N])
