from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
dx =[1,-1,0,0]
dy =[0,0,1,-1]

board = [stdin.readline().rstrip() for _ in range(N)]

def bfs():
    visit = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    queue = deque()
    visit[0][0][0]=True
    queue.append((0,0,1,0))

    while queue:
        x,y,dis,count = queue.popleft()
        if x==N-1 and y==M-1:
            print(dis)
            return
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M :
                if board[nx][ny] == '1' and count == 0:
                    queue.append((nx,ny,dis+1,count+1))
                    visit[1][nx][ny] = True
                elif board[nx][ny] == '0' and not visit[count][nx][ny]:
                    queue.append((nx,ny,dis+1,count))
                    visit[count][nx][ny] = True
    print(-1)

bfs()
