from sys import stdin

N,M = map(int,stdin.readline().split())
board= [[0]*(N+1)]
for _ in range(N):
    board.append([0]+list(map(int,stdin.readline().split())))

print(board)
for i in range(1,N+1):
    for j in range(1,N):
        board[i][j+1]+=board[i][j]

for j in range(1,N+1):
    for i in range(1,N):
        board[i+1][j]+=board[i][j]


for _ in range(M):
    x1,y1,x2,y2 = map(int,stdin.readline().split())
    print(board[x2][y2]-board[x2][y1-1]-board[x1-1][y2]+board[x1-1][y1-1])
