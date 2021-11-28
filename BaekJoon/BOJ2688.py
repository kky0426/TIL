from sys import stdin

T = int(stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(65)]

for i in range(10):
    dp[1][i] = 1

for i in range(2,65):
    for j in range(10):
        for k in range(j,10):
            dp[i][j]+=dp[i-1][k]


for _ in range(T):
    N = int(stdin.readline())
    ans = 0
    for i in range(10):
        ans+=dp[N][i]
    print(ans)
