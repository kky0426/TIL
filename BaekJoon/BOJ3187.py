from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [stdin.readline().rstrip() for _ in range(N)]
wolf = 0
sheep = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'v':
            wolf+=1
        elif board[i][j] == 'k':
            sheep+=1
visit = [[False for _ in range(M)] for _ in range(N)]

def bfs(x,y):
    visit[x][y] = True
    queue = deque()
    queue.append((x,y))
    w = 0
    s = 0
    while queue:
        x,y = queue.popleft()
        if board[x][y] == 'v':
            w+=1
        elif board[x][y] == 'k':
            s+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny]!='#' and not visit[nx][ny]:
                visit[nx][ny]=True
                queue.append((nx,ny))

    global wolf,sheep
    if s>w: wolf-=w
    else: sheep-=s

for i in range(N):
    for j in range(M):
        if board[i][j]!='#' and not visit[i][j]:
            bfs(i,j)

print(sheep,wolf)
