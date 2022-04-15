from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

grid = [list(stdin.readline().rstrip()) for _ in range(2)]
visit = [[False]*N for _ in range(2)]

def bfs():
    queue = deque()
    queue.append((0,0))
    time = -1
    while queue:
        for _ in range(len(queue)):
            d,idx = queue.popleft()
            if idx+1>=N or idx+K>=N:
                return 1

            if grid[d][idx+1] == '1' and not visit[d][idx+1]:
                queue.append((d,idx+1))
                visit[d][idx+1]=True

            if idx-1>time+1 and grid[d][idx-1] == '1' and not visit[d][idx-1]:
                queue.append((d,idx-1))
                visit[d][idx-1] = True

            if grid[(d+1)%2][idx+K] == '1' and not visit[(d+1)%2][idx+K]:
                queue.append(((d+1)%2,idx+K))
                visit[(d+1)%2][idx+K] = True
        time+=1

    return 0

print(bfs())