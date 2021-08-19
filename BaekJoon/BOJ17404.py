from sys import stdin

N = int(stdin.readline())

cost = []
for _ in range(N):
    cost.append(list(map(int,stdin.readline().split())))


dp = [[0 for _ in range(N)] for _ in range(3)]

ans = float("inf")
for color in range(3):

    for i in range(3):
        if i==color:
            dp[i][0]=cost[0][i]
        else:
            dp[i][0] = float("inf")

    for i in range(1,N):
        dp[0][i] = min(dp[1][i-1],dp[2][i-1])+cost[i][0]
        dp[1][i] = min(dp[0][i - 1], dp[2][i - 1]) + cost[i][1]
        dp[2][i] = min(dp[0][i - 1], dp[1][i - 1]) + cost[i][2]

    for i in range(3):
        if i==color:
            continue
        ans = min(ans,dp[i][-1])

print(ans)
