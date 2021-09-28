from sys import stdin

N,M = map(int,stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(N)]

for i in range(1,M):
    board[0][i]+=board[0][i-1]

for i in range(1,N):
    board[i][0]+=board[i-1][0]

for i in range(1,N):
    for j in range(1,M):
        if board[i][j] == 1:
            board[i][j] = max(board[i-1][j],board[i][j-1])+1
        else:
            board[i][j] = max(board[i-1][j],board[i][j-1])

print(board[-1][-1])
