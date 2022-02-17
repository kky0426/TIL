from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())

grid = [list(map(int,stdin.readline().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visit = [[0 for _ in range(M)] for _ in range(N)]

def bfs(x,y,group):
    count = 1
    queue = deque()
    queue.append((x,y))
    visit[x][y] = group
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and grid[nx][ny] == 1:
                visit[nx][ny] = group
                queue.append((nx,ny))
                count+=1
    return count

dic = {}
group = 2
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visit[i][j]:
            dic[group] = bfs(i,j,group)
            group+=1


ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            count = 1
            mem = set()
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<N and 0<=ny<M:
                    mem.add(visit[nx][ny])

            for num in mem:
                if num in dic:
                    count+=dic[num]
            ans = max(ans,count)
print(ans)
