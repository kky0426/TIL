from sys import stdin


while True:
    N = int(stdin.readline())
    if N==0:
        break
        
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N+1):
        dp[0][i] = 1

    for i in range(1,N+1):
        for j in range(i,N+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[-1][-1])
    
