from sys import stdin
from collections import deque
import sys

M,N = map(int,stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [stdin.readline().rstrip() for _ in range(M)]
def bfs(x,y):
    visit[x][y]=True
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        if x==M-1:
            return True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N and not visit[nx][ny] and board[nx][ny]=='0':
                visit[nx][ny] = True
                queue.append((nx,ny))

    return False

visit = [[False for _ in range(N)] for _ in range(M)]

for i in range(N):
    if bfs(0,i):
        print("YES")
        sys.exit(0)
print("NO")
