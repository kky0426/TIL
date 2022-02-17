from sys import stdin
from collections import defaultdict
import heapq

N,P,K = map(int,stdin.readline().split())

graph = defaultdict(list)

for _ in range(P):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(mid):
    queue = []
    distance = [float("inf")] * (N+1)
    heapq.heappush(queue,(0,1))
    distance[1] = 0

    while queue:
        dis,cur = heapq.heappop(queue)
        if distance[cur]<dis:
            continue

        for n,w in graph[cur]:
            cost = 0
            if w > mid:
                cost+=1

            if dis+cost<distance[n]:
                distance[n] = dis+cost
                heapq.heappush(queue,(distance[n],n))

    return distance[N]<=K

left = 0
right = 1000001
ans = -1
while left<=right:
    mid = (left+right)//2
    if dijkstra(mid):
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)
