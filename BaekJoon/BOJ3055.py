from sys import stdin
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

R,C = map(int,stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(R)]

visit = [[0 for _ in range(C)] for _ in range(R)]

water = deque()
queue = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            water.append((i,j))
            visit[i][j] = 1
        elif board[i][j] == 'S':
            queue.append((i,j,0))
        elif board[i][j] == 'D':
            visit[i][j] = 1000000

while water:
    x,y = water.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C and visit[nx][ny]==0 and board[nx][ny]!='X':
            visit[nx][ny] = visit[x][y]+1
            water.append((nx,ny))

go = [[False for _ in range(C)] for _ in range(R)]
ans = -1
while queue:
    x,y,time = queue.popleft()
    if board[x][y] == 'D':
        ans =time
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C and (time<visit[nx][ny]-2 or visit[nx][ny]==0) and not go[nx][ny] and board[nx][ny]!='X':
            go[nx][ny] = True
            queue.append((nx,ny,time+1))

print(ans if ans>0 else "KAKTUS")
