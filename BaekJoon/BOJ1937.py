from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N = int(stdin.readline())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
board = []
dp = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int,stdin.readline().split())))

def dfs(x,y):
    if dp[x][y]:return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[x][y]<board[nx][ny]:
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans,dfs(i,j))
print(ans)
