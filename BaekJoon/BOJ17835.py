from sys import stdin
import heapq
from collections import defaultdict

N,M,K = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[v].append((u,w))

idxs = set(map(int,stdin.readline().split()))

def dijkstra(idxs):
    distance = [float("inf")]*(N+1)
    queue = []
    for idx in idxs:
        distance[idx] = 0
        heapq.heappush(queue,(0,idx))

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if dis+w<distance[n]:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))

    return distance

distance = dijkstra(idxs)
ans = 0
idx = 0
for i in range(1,N+1):
    if distance[i]>ans:
        ans = distance[i]
        idx = i

print(idx)
print(ans)





