from sys import stdin
from collections import deque,defaultdict

N,M = map(int,stdin.readline().split())
dx = [1,1,1,-1,-1,-1,0,0]
dy = [1,-1,0,1,-1,0,1,-1]

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]


def dfs(x,y):
    global flag
    visit[x][y] = True
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if grid[x][y]<grid[nx][ny]:
                flag = False
            if not visit[nx][ny] and grid[x][y] == grid[nx][ny]:
                dfs(nx,ny);
ans = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j] and grid[i][j]>0:
            flag = True
            dfs(i,j)
            if flag:
                ans+=1
print(ans)
