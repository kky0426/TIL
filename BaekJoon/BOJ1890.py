from sys import stdin
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())
grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    
    
    if x==N-1 and y==N-1:
        return 1

    jump = grid[x][y]
    if jump == 0:
        return dp[x][y]
    
    if 0<=y+jump<N:
        dp[x][y]+=dfs(x,y+jump)
    if 0<=x+jump<N:
        dp[x][y]+=dfs(x+jump,y)

    return dp[x][y]

dfs(0,0)
print(dp[0][0])
