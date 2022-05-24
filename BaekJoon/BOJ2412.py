from sys import stdin
import heapq

N,T = map(int, stdin.readline().split())

spot = set(tuple(map(int,stdin.readline().split())) for _ in range(N))

dx = [-2,-1,0,1,2]
dy = [-2,-1,0,1,2]

def bfs(x,y):
    queue  = []
    heapq.heappush(queue,(0,x,y))

    while queue:
        count,x,y = heapq.heappop(queue)
        if y == T:
            return count

        for i in range(5):
            for j in range(5):
                nx = x+dx[i]
                ny = y+dy[j]
                if nx<0 or ny<0:
                    continue
                if (nx,ny) in spot:
                    heapq.heappush(queue,(count+1,nx,ny))
                    spot.remove((nx,ny))
    return -1

print(bfs(0,0))