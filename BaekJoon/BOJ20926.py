from sys import stdin
import heapq

M,N = map(int,stdin.readline().split())

grid = [list(stdin.readline().rstrip()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'T':
            grid[i][j] = 0
            start = (i,j)
        elif grid[i][j] == 'E':
            end = (i,j)
        elif grid[i][j].isdigit():
            grid[i][j] = int(grid[i][j])

distance = [[float("inf") for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

def go(x,y,d):
    count = 1
    while True:
        nx = x+dx[d]*count
        ny = y+dy[d]*count

        if not(0<=nx<N and 0<=ny<M):
            return -1
        if grid[nx][ny] == 'H':
            return -1
        if grid[nx][ny] == 'R':
            return count-1
        if grid[nx][ny] == 'E':
            return count
        count+=1


def solve(x,y):
    queue = []
    heapq.heappush(queue,(0,x,y))
    distance[x][y] = 0
    while queue:
        dis,x,y = heapq.heappop(queue)
        if visit[x][y]:
            continue
        visit[x][y] = True

        for i in range(4):
            count = go(x,y,i)
            if count<1:
                continue
            new_dis = 0
            for j in range(1,count+1):
                if grid[x+dx[i]*j][y+dy[i]*j] == 'E':
                    continue
                new_dis+=grid[x+dx[i]*j][y+dy[i]*j]
            nx = x+dx[i]*count
            ny = y+dy[i]*count

            if distance[nx][ny]>new_dis+dis:
                distance[nx][ny] = new_dis+dis
                heapq.heappush(queue,(distance[nx][ny],nx,ny))

solve(start[0],start[1])
print(distance[end[0]][end[1]] if distance[end[0]][end[1]] != float("inf") else -1)
