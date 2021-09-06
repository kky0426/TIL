from sys import stdin

N,M = map(int,stdin.readline().split())


direction = [(-1,1),(0,1),(1,1)]
visit = [[False for _ in range(M)] for _ in range(N)]
board = [stdin.readline().rstrip() for _ in range(N)]
ans = 0
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M or board[x][y] == "x" or visit[x][y] == True:
        return False

    visit[x][y] = True
    if y == M-1:
        return True


    for i in range(3):
        nx = x+direction[i][0]
        ny = y+direction[i][1]
        if dfs(nx,ny):
            return True

for i in range(N):
    if dfs(i,0):
        ans+=1

print(ans)
