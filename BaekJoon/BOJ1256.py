from sys import stdin

N,M,K = map(int,stdin.readline().split())

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    dp[i][0] = 1

for i in range(1,M+1):
    dp[0][i] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=dp[i-1][j] + dp[i][j-1]

if dp[-1][-1] < K:
    print(-1)
else:
    ans = ""
    while True:
        if N==0 or M==0:
            ans+="a"*N
            ans+="z"*M
            break

        flag = dp[N-1][M]

        if flag>=K:
            ans+="a"
            N-=1
        else:
            ans+="z"
            M-=1
            K-=flag
    print(ans)
