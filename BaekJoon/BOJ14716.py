from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
board = [list(map(int,stdin.readline().split())) for _ in range(N)]

dx = [1,1,1,-1,-1,-1,0,0]
dy = [1,0,-1,1,0,-1,1,-1]

def bfs(x,y):
   queue = deque()
   queue.append((x,y))
   while queue:
       x,y = queue.popleft()
       for i in range(8):
           nx = x+dx[i]
           ny = y+dy[i]
           if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
               queue.append((nx,ny))
               board[nx][ny] = 0

ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i,j)
            ans+=1

print(ans)
