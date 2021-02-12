import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

tomato = [sys.stdin.readline().rstrip().split() for _ in range(M)]
flag=0
for line in tomato:
    if '0' in line:
        flag=1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[j][i] == '1':
            queue.append([j, i])

day = 0

while queue:
    day += 1
    for j in range(len(queue)):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and tomato[nx][ny] == '0':
                tomato[nx][ny] = '1'
                queue.append([nx, ny])

for line in tomato:
    if '0' in line:
        flag=2


if flag == 0:
    print(0)
elif flag == 2:
    print(-1)
else:
    print(day-1)
