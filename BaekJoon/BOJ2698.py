from sys import stdin

dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
dp[1][0][1] = 1
dp[1][0][0] = 1
for k in range(101):
    for n in range(2,101):
        if k == 0:
            dp[n][k][1]+=dp[n-1][k][0]
        else:
            dp[n][k][1]+=dp[n-1][k][0]+dp[n-1][k-1][1]
        dp[n][k][0]+=dp[n-1][k][0]+dp[n-1][k][1]

N = int(stdin.readline())
for _ in range(N):
    N,K = map(int,stdin.readline().split())
    print(sum(dp[N][K]))
