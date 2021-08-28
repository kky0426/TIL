from sys import stdin

dx=[1,-1,0,0]
dy=[0,0,1,-1]

board = [list(map(str,stdin.readline().split())) for _ in range(5)]

ans = set()
def dfs(x,y,word):

    if len(word)==6:
        ans.add(word)
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,word+board[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])

print(len(ans))
