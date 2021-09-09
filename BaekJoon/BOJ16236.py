from sys import stdin
from collections import deque

N = int(stdin.readline())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
board = []
for i in range(N):
    line = list(map(int,stdin.readline().split()))
    board.append(line)
    for j in range(N):
        if line[j] == 9:
            start_x = i
            start_y = j

board[start_x][start_y] = 0

def bfs(x,y,weight):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[x][y] = True
    queue = deque()
    queue.append((x,y,0))

    while queue:
        fish = []
        for _ in range(len(queue)):
            x,y,dis = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N and board[nx][ny]<=weight and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx,ny,dis+1))
                    if 0<board[nx][ny]<weight:
                        fish.append((nx,ny,dis+1))

        if fish:
            fish.sort(key=lambda x:(x[2],x[0],x[1]))
            return fish[0][0],fish[0][1],fish[0][2]

    return -1,-1,-1

time = 0
weight=2
count = 0
while True:
    x,y,dis = bfs(start_x,start_y,weight)
    if dis == -1:
        print(time)
        break
    time+=dis
    board[x][y] = 0
    count+=1
    if count == weight:
        weight+=1
        count=0
    start_x = x
    start_y = y
