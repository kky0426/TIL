from sys import stdin

N,M = map(int,stdin.readline().split())

grid = [list(stdin.readline()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(x,y):
    count = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and grid[nx][ny] == '.':
            count+=1
    if count<=1:
        return True
    return False

def solve():
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                if check(i,j):
                   return False
    return True

if solve():
    print(0)
else:
    print(1)
