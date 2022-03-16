from sys import stdin
from collections import deque
N,M,T = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

x1 = x2 = 0
for i in range(N):
    if grid[i][0] == -1:
        if x1 == 0:
            x1 = i
        else:
            x2 = i

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def spread():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j]>0:
                queue.append((i,j,grid[i][j]))

    while queue:
        x,y,w = queue.popleft()

        count = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and grid[nx][ny]!=-1:
                grid[nx][ny]+=w//5
                count+=1
        grid[x][y]-=(w//5)*count

def rotate_top():
    r1,c1,r2,c2 = 0,0,x1,M-1
    for i in range(r2,r1,-1):
        grid[i][c1] = grid[i-1][c1]
    grid[r2][c1] = 0
    for i in range(c1,c2):
        grid[r1][i] = grid[r1][i+1]

    for i in range(r1,r2):
        grid[i][c2] = grid[i+1][c2]

    for i in range(c2,c1,-1):
        grid[r2][i] = grid[r2][i-1]
    grid[r2][c1] = -1

def rotate_bottom():
    r1,c1,r2,c2 = x2,0,N-1,M-1
    for i in range(r1,r2):
        grid[i][c1] = grid[i+1][c1]
    grid[r1][c1] = 0
    for i in range(c1,c2):
        grid[r2][i] = grid[r2][i+1]

    for i in range(r2,r1,-1):
        grid[i][c2] = grid[i-1][c2]

    for i in range(c2,c1,-1):
        grid[r1][i] = grid[r1][i-1]

    grid[r1][c1] = -1


for _ in range(T):
    spread()
    rotate_top()
    rotate_bottom()

ans = 2
for arr in grid:
    ans+=sum(arr)

print(ans)