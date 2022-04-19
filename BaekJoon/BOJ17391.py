from sys import stdin
from collections import deque
N,M = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[0][0] = True
    while queue:
        count,x,y = queue.popleft()
        if x==N-1 and y==M-1:
            return count

        move = grid[x][y]
        for i in range(1,move+1):
            if x+i<N and not visit[x+i][y]:
                queue.append((count+1,x+i,y))
                visit[x+i][y] = True
            if y+i<M and not visit[x][y+i]:
                queue.append((count+1,x,y+i))
                visit[x][y+i] = True

print(bfs())
