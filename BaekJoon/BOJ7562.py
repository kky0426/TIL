from sys import stdin
from collections import deque

d = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]

def bfs(x,y):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[x][y] = True
    queue = deque()
    queue.append((x,y,0))
    while queue:
        x,y,count = queue.popleft()
        if x==end_x and y==end_y:
            return count
        for i in range(8):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny,count+1))

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    start_x,start_y = map(int,stdin.readline().split())
    end_x,end_y = map(int,stdin.readline().split())
    print(bfs(start_x,start_y))
