from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[0][0] = 1
    if N == 0:
        print(dp[0][0],dp[0][1])
        continue
    dp[1][1] = 1

    for i in range(2,N+1):
        dp[i][0] = dp[i-1][0]+dp[i-2][0]
        dp[i][1] = dp[i-1][1]+dp[i-2][1]

    print(dp[-1][0],dp[-1][1])
