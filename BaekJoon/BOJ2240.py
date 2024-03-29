from sys import stdin

T,W = map(int,stdin.readline().split())

drop = [int(stdin.readline()) for _ in range(T)]
dp = [[0 for _ in range(W+1)] for _ in range(T+1)]

for i in range(1,T+1):
    for j in range(W+1):
        if j == 0:
            if drop[i-1] == 1:
                dp[i][0] = dp[i-1][0]+1
            else:
                dp[i][0] = dp[i-1][0]
        else:
            if drop[i-1] == 1 and j%2 == 0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+1
            elif drop[i-1] == 2 and j%2 == 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[-1]))
