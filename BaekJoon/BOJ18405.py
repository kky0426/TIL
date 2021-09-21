from sys import stdin
from collections import deque

N ,K= map(int,stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = []


board = [list(map(int,stdin.readline().split())) for _ in range(N)]
S,X,Y = map(int,stdin.readline().split())

for i in range(N):
    for j in range(N):
        if board[i][j]>0:
            queue.append((board[i][j],i,j,0))

queue = deque(sorted(queue,key = lambda x:x[0]))

while queue:
    _,x,y,time = queue.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            board[nx][ny] = board[x][y]
            queue.append((0,nx,ny,time+1))

print(board[X-1][Y-1])
