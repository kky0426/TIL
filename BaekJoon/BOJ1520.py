from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N,M = map(int,stdin.readline().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

board = []
for _ in range(N):
    board.append(list(map(int,stdin.readline().split())))

ans = 0

dp = [[0 for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]


def dfs(x,y):
    if visit[x][y]:
        return dp[x][y]
    if x==N-1 and y==M-1:
        return 1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and board[x][y]>board[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    visit[x][y] = True
    return dp[x][y]
dfs(0,0)
print(dp[0][0])
