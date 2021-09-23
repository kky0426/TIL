from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = []
virus = []

wall = 0
for i in range(N):
    line = list(map(int, stdin.readline().split()))
    board.append(line)
    for j in range(N):
        if line[j] == 2:
            virus.append((i, j))
        elif line[j] == 1:
            wall+=1

def combinations(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i + 1:], n - 1):
                yield [arr[i]] + next


def bfs(queue,visit):
    ans = 0
    count = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1:
                if board[nx][ny] != 1:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx,ny))

    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1:
                count+=1

    if count == wall:
        for i in range(N):
            for j in range(N):
                if board[i][j]!=1 and (i,j) not in virus:
                    ans = max(ans,visit[i][j])
        return ans
    else:
        return float("inf")



answer = float("inf")
for candidate in combinations(virus, M):
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    for x,y in candidate:
        visit[x][y] = 0

    answer = min(answer,bfs(deque(candidate),visit))


print(answer if answer != float("inf") else -1)
