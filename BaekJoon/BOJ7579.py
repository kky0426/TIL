from sys import stdin

N,M = map(int,stdin.readline().split())

Bytes = list(map(int,stdin.readline().split()))
costs = list(map(int,stdin.readline().split()))

dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)]
result = sum(costs)

for i in range(1,N+1):
    byte = Bytes[i-1]
    cost = costs[i-1]
    for j in range(1,sum(costs)+1):
        if j<cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost]+byte)

        if dp[i][j] >= M:
            result = min(result,j)


print(result if M!=0 else 0)
