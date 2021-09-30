from sys import stdin
from collections import deque

N = int(stdin.readline())
r1,c1,r2,c2 = map(int,stdin.readline().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x,y):
    visit=[[False for _ in range(N)] for _ in range(N)]
    visit[x][y] = True
    queue = deque()
    queue.append((x,y,0))
    while queue:
        x,y,count = queue.popleft()
        if x==r2 and y==c2:
            return count
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                queue.append((nx,ny,count+1))
                visit[nx][ny] = True
    return -1
print(bfs(r1,c1))
