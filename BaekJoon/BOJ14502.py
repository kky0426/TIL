from sys import stdin
from collections import deque
import copy

board=[]
empty=[]
virus=[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M = map(int,stdin.readline().split())

for i in range(N):
    line = list(map(int,stdin.readline().split()))
    board.append(line)
    for j in range(len(line)):
        if line[j]==0:
            empty.append((i,j))
        elif line[j] == 2:
            virus.append((i,j))
            
def bfs(board,x,y):
    queue=deque()
    queue.append((x,y))
    visit = set()
    visit.add((x,y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny]==0 and not (nx,ny) in visit:
                board[nx][ny] = 2
                queue.append((nx,ny))
                visit.add((nx,ny))
ans = 0
for i in range(2,len(empty)):
    for j in range(i):
        for k in range(j):
            count = 0
            x1,y1 = empty[i]
            x2,y2 = empty[j]
            x3,y3 = empty[k]

            board[x1][y1] = 2
            board[x2][y2] = 2
            board[x3][y3] = 2

            temp = copy.deepcopy(board)
            for x,y in virus:
                bfs(temp,x,y)
            for line in temp:
                count+=line.count(0)
            ans = max(ans,count)

            board[x1][y1] = 0
            board[x2][y2] = 0
            board[x3][y3] = 0

print(ans)
