from sys import stdin
from collections import deque

N,M,K = map(int,stdin.readline().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x,y = map(int,stdin.readline().split())
    board[x-1][y-1] = 1

def bfs(x,y):
    queue = deque()
    board[x][y] = 0
    queue.append((x,y))
    count =1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx,ny))
                count+=1
    return count

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            ans = max(ans,bfs(i,j))
print(ans)
