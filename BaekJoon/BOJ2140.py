from sys import stdin

N = int(stdin.readline())

grid = []
boom = []

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,-1,0,1,-1,1,-1,0]

for i in range(N):
    line = stdin.readline().rstrip()
    temp = []
    for j in range(N):
        if line[j] == '#':
            temp.append(-1)
            boom.append((i,j))
        else:
            temp.append(int(line[j]))
    grid.append(temp)

def check(x,y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if grid[nx][ny] == 0:
                return False
    return True

def minus(x,y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and grid[nx][ny]>0:
            grid[nx][ny]-=1

ans = 0

while boom:
    x,y = boom.pop()
    if check(x,y):
        ans+=1
        minus(x,y)
print(ans)
