from sys import stdin

N,M = map(int,stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int,stdin.readline().split())))

for i in range(1,M):
    board[0][i]+=board[0][i-1]

for i in range(1,N):
    board[i][0]+=board[i-1][0]

for i in range(1,N):
    for j in range(1,M):
        board[i][j]+=max(board[i][j-1],board[i-1][j],board[i-1][j-1])

print(board[-1][-1])
