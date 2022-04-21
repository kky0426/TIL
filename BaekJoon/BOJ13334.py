from sys import stdin
import heapq

N = int(stdin.readline())

road  = [list(map(int,stdin.readline().split())) for _ in range(N)]
d = int(stdin.readline())
for i in range(N):
    if road[i][0] > road[i][1]:
        road[i][0],road[i][1] = road[i][1],road[i][0]
road.sort(key=lambda x:x[1])

queue = []
ans = 0
for s,e in road:
    heapq.heappush(queue,s)
    while queue and queue[0] < e-d:
        heapq.heappop(queue)
    ans = max(ans,len(queue))

print(ans)