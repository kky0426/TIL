from sys import stdin
from collections import deque

N,M,K = map(int,stdin.readline().split())
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
food = [list(map(int,stdin.readline().split())) for _ in range(N)]
board = [[5 for _ in range(N)] for _ in range(N)]
queue = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int,stdin.readline().split())
    queue[x-1][y-1].append(z)


for _ in range(K):
    death = []
    #봄
    for i in range(N):
        for j in range(N):
            for _ in range(len(queue[i][j])):
                z = queue[i][j].popleft()
                if board[i][j]>=z:
                    board[i][j]-=z
                    queue[i][j].append(z+1)
                else:
                    death.append((i,j,z))

    #여름
    while death:
        x,y,z = death.pop()
        board[x][y]+=z//2

    #가을
    for i in range(N):
        for j in range(N):
            for z in queue[i][j]:
                if z%5 == 0:
                    for k in range(8):
                        nx = i+dx[k]
                        ny = j+dy[k]
                        if 0<=nx<N and 0<=ny<N:
                            queue[nx][ny].appendleft(1)
    #겨울
    for i in range(N):
        for j in range(N):
            board[i][j]+=food[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans+=len(queue[i][j])

print(ans)
