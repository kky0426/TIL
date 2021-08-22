from sys import stdin
from collections import deque

C,R,H = map(int,stdin.readline().split())

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
visit = [[[0 for _ in range(C)] for _ in range(R)]]*H
queue = deque()
boxes = []
for z in range(H):
    temp = []
    for x in range(R):
        line=list(map(int,stdin.readline().split()))
        temp.append(line)
        for y in range(C):
            if line[y] == 1:
                queue.append((x,y,z))
    boxes.append(temp)

def bfs():
    while queue:
        x,y,z = queue.popleft()
        visit[z][x][y] = 1
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<R and 0<=ny<C and 0<=nz<H and not boxes[nz][nx][ny]:
                queue.append((nx,ny,nz))
                boxes[nz][nx][ny] = boxes[z][x][y]+1
                visit[nz][nx][ny] = 1

bfs()

ans=0
flag = False
for i in range(R):
    for j in range(C):
        for k in range(H):
            if boxes[k][i][j]==0:
                flag=True
                break
            ans = max(ans,boxes[k][i][j])

print(ans-1 if not flag else -1)
