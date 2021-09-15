from sys import stdin
from collections import deque

direction = [(0,1),(1,0),(0,-1),(-1,0)]
N = int(stdin.readline())
K = int(stdin.readline())

board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x,y = map(int,stdin.readline().split())
    board[x-1][y-1] = 1


L = int(stdin.readline())
command = [list(stdin.readline().rstrip().split()) for _ in range(L)]
command = deque(command)

head = 0
time = 0
snake = deque()
snake.append((0,0))

while True:
    time+=1
    nx = snake[-1][0]+direction[head%4][0]
    ny = snake[-1][1]+direction[head%4][1]
    if 0<=nx<N and 0<=ny<N and (nx,ny) not in snake:
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            snake.append((nx,ny))
        else:
            snake.append((nx,ny))
            snake.popleft()
    else:
        break

    if command and int(command[0][0]) == time:
        if command[0][1] == 'D':
            head+=1
        else:
            head-=1
        command.popleft()

print(time)
