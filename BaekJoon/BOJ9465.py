from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())

    up = list(map(int,stdin.readline().split()))
    down = list(map(int,stdin.readline().split()))
    dp = [[0 for _ in range(2)] for _ in range(N+1)]

    dp[1][0]=up[0]
    dp[1][1]=down[0]
    for i in range(2,N+1):
        dp[i][0] = max(dp[i-2][0],dp[i-2][1],dp[i-1][1])+up[i-1]
        dp[i][1] = max(dp[i-2][1],dp[i-2][0],dp[i-1][0])+down[i-1]

    print(max(dp[-1])
