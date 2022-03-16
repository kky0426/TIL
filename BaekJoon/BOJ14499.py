from sys import stdin

N,M,x,y,K = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

command = list(map(int,stdin.readline().split()))

dice = [0,0,0,0,0,0]
# 1 5 6 2 3 4
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def roll(r,c,d):
    nx = r+dx[d]
    ny = c+dy[d]
    if not(0<=nx<N and 0<=ny<M):
        return

    if d == 0:
        dice[0],dice[4],dice[2],dice[5] = dice[5],dice[0],dice[4],dice[2]
    elif d == 1:
        dice[0],dice[4],dice[2],dice[5] = dice[4],dice[2],dice[5],dice[0]
    elif d == 3:
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
    elif d == 2:
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]

    if grid[nx][ny] == 0:
        grid[nx][ny] = dice[2]
    else:
        dice[2] = grid[nx][ny]
        grid[nx][ny] = 0

    print(dice[0])
    global x,y
    x = nx
    y = ny

for d in command:
    roll(x,y,d-1)
