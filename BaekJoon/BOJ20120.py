from sys import stdin

N = int(stdin.readline())
points =[0]+list(map(int,stdin.readline().split()))

dp = [[-float("inf") for _ in range(N+1)] for _ in range(N+1)]

dp[1][1] = points[1]
dp[1][0] = 0

for i in range(1,N):
    for j in range(i+1):
        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+points[i+1]*(j+1))

        if i+2>N:
            dp[N][0] = max(dp[N][0],dp[i][j])
            continue
        dp[i+2][1] = max(dp[i+2][1],dp[i][j]+points[i+2])

        if i+3>N:
            dp[N][0] = max(dp[N][0],dp[i][j])
            continue

        if i==1 and j==0:
            continue
        dp[i+3][1] = max(dp[i+3][1],dp[i][j]+points[i+3])

ans = 0
for i in range(N+1):
    ans = max(ans,dp[N][i])

print(ans)


