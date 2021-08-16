from sys import stdin

K,N = map(int,stdin.readline().split())

values = []
times = []

for _ in range(N):
    l,t = map(int,stdin.readline().split())
    values.append(l)
    times.append(t)

dp = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N):
    time = times[i]
    value = values[i]
    for j in range(1,K+1):
        if j<time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-time]+value)

print(dp[-1][-1])
