from sys import stdin
from collections import deque

K = int(stdin.readline())

M,N = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ddx = [2,2,1,1,-2,-2,-1,-1]
ddy = [-1,1,2,-2,1,-1,2,-2]
visit = [[[False for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0,0,0,0))

    while queue:
        x,y,count,dis = queue.popleft()
        if x == N-1 and y == M-1:
            return dis

        if count<K:
            for i in range(8):
                nx = x+ddx[i]
                ny = y+ddy[i]
                if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 0 and not visit[nx][ny][count+1]:
                    visit[nx][ny][count+1] = True
                    queue.append((nx,ny,count+1,dis+1))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 0 and not visit[nx][ny][count]:
                visit[nx][ny][count] = True
                queue.append((nx,ny,count,dis+1))

    return -1

print(bfs())





