from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

board = [list(map(int,stdin.readline().split())) for _ in range(N)]


def check(x,y):
    count = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0:
            count+=1
    return count

def bfs(x,y,visit):
    queue = deque()
    visit[x][y]=True
    queue.append((x,y))
    melt = []
    melt.append((x,y,check(x,y)))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and board[nx][ny]>0:
                visit[nx][ny]=True
                queue.append((nx,ny))
                melt.append((nx,ny,check(nx,ny)))

    for x,y,count in melt:
        board[x][y] = max(board[x][y]-count,0)

time = 0
while True:
    division = 0
    visit = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j]>0 and not visit[i][j]:
                division+=1
                bfs(i,j,visit)

    if division == 0:
        time = 0
        break
    if division>=2:
        break
    time+=1
print(time)
