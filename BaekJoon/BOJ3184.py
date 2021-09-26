from sys import stdin
from collections import deque

R,C = map(int,stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [list(stdin.readline().rstrip()) for _ in range(R)]
wolf= 0
sheep = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == 'v':
            wolf+=1
        elif board[i][j]== 'o':
            sheep+=1
visit = [[False for _ in range(C)] for _ in range(R)]
def bfs(x,y):
    visit[x][y] = True
    queue = deque()
    queue.append((x,y))
    w=0
    s=0
    while queue:
        x,y = queue.popleft()
        if board[x][y]=='v':
            w+=1
        elif board[x][y] =='o':
            s+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C and not visit[nx][ny] and board[nx][ny]!='#':
                visit[nx][ny] = True
                queue.append((nx,ny))

    if s>w:
        global wolf
        wolf-=w
    else:
        global sheep
        sheep-=s

for i in range(R):
    for j in range(C):
        if board[i][j]!='#' and not visit[i][j]:
            bfs(i,j)

print(sheep,wolf)
