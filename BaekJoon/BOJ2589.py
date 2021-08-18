from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
board=[]
for _ in range(N):
    board.append(stdin.readline().rstrip())

def bfs(x,y):
    visit = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    queue = deque()
    queue.append((x,y,0))
    visit[x][y] = True

    while queue:
        x,y,dis = queue.popleft()
        count = max(count,dis)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny]=="L" and not visit[nx][ny]:
                queue.append((nx,ny,dis+1))
                visit[nx][ny]=True
    return count

ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            ans = max(ans,bfs(i,j))


print(ans)
