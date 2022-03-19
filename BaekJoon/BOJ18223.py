from sys import stdin
from collections import defaultdict
import heapq


V,E,P = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(E):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(start,end):
    queue = []
    distance = [float("inf")]*(V+1)
    distance[start] = 0
    heapq.heappush(queue,(0,start))

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if distance[n]>dis+w:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))

    return distance[end]

if dijkstra(1,V) == dijkstra(1,P)+dijkstra(P,V):
    print("SAVE HIM")
else:
    print("GOOD BYE")