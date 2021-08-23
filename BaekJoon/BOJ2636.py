from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
board=[list(map(int,stdin.readline().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[0][0] = True
    queue=deque()
    queue.append((0,0))
    count = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                if board[nx][ny] == 0:
                    visit[nx][ny] = True
                    queue.append((nx,ny))
                elif board[nx][ny] == 1:
                    visit[nx][ny] = True
                    board[nx][ny] = 0
                    count+=1
    return count
time=0
count_list=[]
while True:
    time+=1
    count = bfs()
    if count == 0:
        break
    count_list.append(count)

print(time-1)
print(count_list[-1])
