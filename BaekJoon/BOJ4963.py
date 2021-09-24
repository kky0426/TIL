from sys import stdin
from collections import deque

dx = [1,1,1,-1,-1,-1,0,0]
dy = [0,1,-1,0,1,-1,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    board[x][y]=0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny]=0
                queue.append((nx,ny))

while True:
    M,N = map(int,stdin.readline().split())
    if N==0 and M == 0:
        break
    ans = 0
    board = [list(map(int,stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i,j)
                ans+=1
    print(ans)
