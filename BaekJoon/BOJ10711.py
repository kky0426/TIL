from sys import stdin
from collections import deque

direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

N,M = map(int,stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == '.':
            board[i][j] = 0
            queue.append((i,j))
        else:
            board[i][j] = int(board[i][j])

visit = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
while queue:
    x,y = queue.popleft()
    for i in range(8):
        nx = x+direction[i][0]
        ny = y+direction[i][1]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] != 0:
                board[nx][ny]-=1
                if board[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    ans = max(ans,visit[nx][ny])
                    queue.append((nx,ny))

print(ans)
