from sys import stdin
from collections import deque

N,M,K = map(int,stdin.readline().split())
board = [[0 for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def square(x1,y1,x2,y2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 1

for _ in range(K):
    x1,y1,x2,y2 = map(int,stdin.readline().split())
    square(x1,y1,x2,y2)

def bfs(x,y):
    queue = deque()
    board[x][y] = 2
    queue.append((x,y))
    S = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx,ny))
                S+=1
    return S

count = 0
ans=[]

for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            ans.append(bfs(i,j))
            count+=1
ans.sort()
print(count)
print(" ".join(map(str,ans)))
