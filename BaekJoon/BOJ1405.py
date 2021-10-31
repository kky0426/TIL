from sys import stdin

K,E,W,N,S = map(int,stdin.readline().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = [N,E,S,W]
visit = [[False for _ in range(2*K+1)] for _ in range(2*K+1)]
ans = 0
def dfs(K,x,y,prob):
    if K == 0:
        global ans
        ans+=prob
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        np = prob*(direction[i]/100)
        if visit[nx][ny]:
            continue
        visit[nx][ny] = True
        dfs(K-1,nx,ny,np)
        visit[nx][ny] = False

visit[K][K] = True
dfs(K,K,K,1)
print(ans)
