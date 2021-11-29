from sys import stdin

R,C,K = map(int,stdin.readline().split())

grid = [list(stdin.readline()) for _ in range(R)]

visit = [[False for _ in range(C)] for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0
def go(x,y,count):
    if x==0 and y==C-1 and count == K:
        global ans
        ans+=1
        return
    if count>K:
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C and grid[nx][ny] == '.' and not visit[nx][ny]:
            visit[nx][ny]=True
            go(nx,ny,count+1)
            visit[nx][ny]=False
visit[R-1][0]=True
go(R-1,0,1)
print(ans)
