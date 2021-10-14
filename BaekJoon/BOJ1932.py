from sys import stdin

N = int(stdin.readline())

dp = [[0 for _ in range(i)] for i in range(1,N+1)]

board=[]
for i in range(N):
    row = list(map(int,stdin.readline().split()))
    board.append(row)

dp[0][0] = board[0][0]

if N == 1:
    print(dp[0][0])
else:
    for i in range(1,N):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = max(dp[i][j],dp[i-1][j]+board[i][j])
            elif j == len(dp[i])-1:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+board[i][j])
            else:
                dp[i][j]= max(dp[i][j],dp[i-1][j]+board[i][j],dp[i-1][j-1]+board[i][j])

    print(max(dp[-1]))
