from sys import stdin
from collections import deque
from itertools import combinations
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M = map(int,stdin.readline().split())

board = []
virus=[]
for i in range(N):
    line = list(map(int,stdin.readline().split()))
    board.append(line)
    for j in range(N):
        if line[j] == 2:
            virus.append((i,j))

def bfs(spot,board):
    visit = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    for x,y in spot:
        queue.append((x,y))
        visit[x][y] = True
        board[x][y] = -1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny] and board[nx][ny]!=1:
                board[nx][ny]=board[x][y]-1
                queue.append((nx,ny))
                visit[nx][ny]=True

candidate = list(combinations(virus,M))

ans = -float("inf")
for spot in candidate:
    count = 0
    temp = copy.deepcopy(board)
    bfs(spot,temp)
    flag = False
    for line in temp:
        count = min(count,min(line))
        if line.count(0)>0:
            flag=True
            break

    if not flag:
        ans = max(ans, count)


print(-ans-1 if ans!=-float("inf") else -1)
