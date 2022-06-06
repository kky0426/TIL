from sys import stdin
import heapq
from collections import defaultdict

N,M,X,Y = map(int,stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))


def dijkstra(start):
    distance = [float("inf")]*N
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node] < dis:
            continue

        for n,w in graph[node]:
            if dis+w<distance[n]:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))
    return distance

distance = dijkstra(Y)
pre = 0
ans = 1
distance.sort()
for i in range(N):
    if distance[i]*2>X:
        ans = float("inf")
        break
    if pre+distance[i]*2<=X:
        pre+=distance[i]*2
    else:
        ans+=1
        pre = distance[i]*2
print(ans if ans!=float("inf") else -1)