from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N,M = map(int,stdin.readline().split())

visit = [[-1 for _ in range(M)] for _ in range(N)]
grid = [list(stdin.readline().rstrip()) for _ in range(N)]

def dfs(x,y):
    if not (0<=x<N and 0<=y<M):
        return 1

    if visit[x][y]>=0:
        return visit[x][y]
    visit[x][y] = 0
    if grid[x][y] == 'U':
        visit[x][y]=dfs(x-1,y)
    elif grid[x][y] == 'R':
        visit[x][y]=dfs(x,y+1)
    elif grid[x][y] == 'D':
        visit[x][y]=dfs(x+1,y)
    else:
        visit[x][y]=dfs(x,y-1)

    return visit[x][y]

ans = 0
for i in range(N):
    for j in range(M):
        ans+=dfs(i,j)

print(ans)
