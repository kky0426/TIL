from sys import stdin
from collections import deque

N,L,R = map(int,stdin.readline().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [list(map(int,stdin.readline().split())) for _ in range(N)]

def bfs(x,y):
    queue = deque()
    visit[x][y] = True
    queue.append((x,y))
    union = [(x,y)]
    total = board[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if L<=abs(board[x][y]-board[nx][ny])<=R and not visit[nx][ny]:
                    queue.append((nx,ny))
                    union.append((nx,ny))
                    total+=board[nx][ny]
                    visit[nx][ny] = True
    if len(union)<=1:
        return 0

    l = len(union)
    while union:
        x,y = union.pop()
        board[x][y] = total//l
    return l
time = 0

while True:
    visit = [[False for _ in range(N)] for _ in range(N)]
    union = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                union+=bfs(i,j)

    if union == 0:
        print(time)
        break
    time+=1
