import sys

n, m = map(int, sys.stdin.readline().split())

visit = [[0] * m for _ in range(n)]

miro=[sys.stdin.readline().rstrip() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0,0, 1, -1]

queue = [(0, 0)]
visit[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == n - 1 and y == m - 1:
        print(visit[x][y])
        break

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < m:
            if visit[next_x][next_y] == 0 and miro[next_x][next_y] == '1':
                visit[next_x][next_y] = visit[x][y] + 1
                queue.append((next_x, next_y))