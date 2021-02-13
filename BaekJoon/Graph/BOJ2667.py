#dfs

N = int(input())
apt = []
for i in range(N):
    apt.append(list(map(int, input())))


def dfs(x, y, count):

    apt[x][y] = 0
    dx = [1,- 1,0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and apt[nx][ny] == 1:
            count = dfs(nx, ny, count + 1)

    return count


answer = []
for i in range(N):
    for j in range(N):
        if apt[i][j]==1:
            answer.append(dfs(i, j, 1))

answer.sort()
print(len(answer))
for i in answer:
    print(i)

#bfs
'''
from collections import deque

N = int(input())
apt = []
for i in range(N):
    apt.append(list(map(int, input())))


def bfs(x, y):
    queue=deque()
    queue.append((x,y))
    apt[x][y] = 0
    dx = [1,- 1,0, 0]
    dy = [0, 0, 1, -1]
    count=1
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and apt[nx][ny] == 1:
                count+=1
                apt[nx][ny]=0
                queue.append((nx,ny))

    return count


answer = []
for i in range(N):
    for j in range(N):
        if apt[i][j]==1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)
'''
