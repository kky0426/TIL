from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[0][0] = True
    queue = deque()
    queue.append((0,0))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                if grid[nx][ny]>=1:
                    grid[nx][ny]+=1
                else:
                    visit[nx][ny] = True
                    queue.append((nx,ny))






def check():
    flag = True
    for i in range(N):
        for j in range(M):
            if grid[i][j]>=3:
                grid[i][j] = 0
            elif grid[i][j]>0:
                flag=False
                grid[i][j] = 1

    return flag

ans = 0

while True:
    ans+=1
    bfs()
    if check():
        break

print(ans)