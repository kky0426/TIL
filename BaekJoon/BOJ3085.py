from sys import stdin

N = int(stdin.readline())

grid = [list(stdin.readline().rstrip()) for _ in range(N)]

def check_row(x):
    count = 1
    res = 0
    for j in range(N-1):
        if grid[x][j] == grid[x][j+1]:
            count+=1
        else:
            count = 1
        res = max(res,count)
    return res

def check_col(y):
    count = 1
    res = 0
    for i in range(N-1):
        if grid[i][y] == grid[i+1][y]:
            count+=1
        else:
            count = 1
        res = max(res,count)
    return res

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
for x in range(N):
    for y in range(N):
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                ans = max(ans,check_row(x),check_col(y))
                grid[x][y],grid[nx][ny] = grid[nx][ny],grid[x][y]
                ans = max(ans,check_row(x),check_col(y))
                grid[x][y],grid[nx][ny] = grid[nx][ny],grid[x][y]

print(ans)