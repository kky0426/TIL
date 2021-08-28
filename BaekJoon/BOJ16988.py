from sys import stdin
from collections import deque
from itertools import combinations

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M = map(int,stdin.readline().split())

board = []
empty = []

for i in range(N):
    line = list(map(int,stdin.readline().split()))
    board.append(line)
    for j in range(M):
        if line[j] == 0:
            empty.append((i,j))

def bfs(x,y,visit):
    flag = False
    queue = deque()
    queue.append((x,y))
    count = 1
    visit[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0:
                    flag = True
                elif board[nx][ny]==2 and not visit[nx][ny]:
                    visit[nx][ny]=True
                    queue.append((nx,ny))
                    count+=1

    if flag:
        return 0

    return count

candidates = list(combinations(empty,2))
ans = 0
for candidate in candidates:
    count = 0
    for x,y in candidate:
        board[x][y] = 1

    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]==2 and not visit[i][j]:
                count+=bfs(i,j,visit)
    ans = max(ans,count)
    for x,y in candidate:
        board[x][y] = 0

print(ans)
