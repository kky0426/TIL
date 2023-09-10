from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]
not_available = set()

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit = [[False for _ in range(M)] for _ in range(N)]

    visit[x][y] = True
    grid[x][y] = 0
    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            nx = current_x+dx[i]
            ny = current_y+dy[i]
            if 0<=nx<N and 0<=ny<M and (nx,ny) not in not_available and not visit[nx][ny]:
                visit[nx][ny]=True
                grid[nx][ny] = grid[current_x][current_y]+1
                queue.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visit[i][j]:
                grid[i][j] = -1

for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            start_x = i
            start_y = j
        elif grid[i][j] == 0:
            not_available.add((i,j))

bfs(start_x,start_y)


for line in grid:
    print(*line)
