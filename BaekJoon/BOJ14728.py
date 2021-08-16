from sys import stdin

N,T = map(int,stdin.readline().split())

times = []
points = []
for _ in range(N):
    t,p = map(int,stdin.readline().split())
    times.append(t)
    points.append(p)

dp = [[0 for _ in range(T+1)] for _ in range(N)]

for i in range(N):
    time = times[i]
    point = points[i]
    for j in range(1,T+1):
        if j-time<0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-time]+point)

print(dp[-1][-1])
