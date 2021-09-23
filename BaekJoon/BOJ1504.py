from sys import stdin
import heapq
from collections import defaultdict

N,E = map(int, stdin.readline().split())

graph = defaultdict(list)
for _ in range(E):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

v1,v2 = map(int,stdin.readline().split())

def dijkstra(start,end):
    distance = [float("inf")]*(N+1)
    distance[start] = 0

    heap = [(0,start)]
    while heap:
        dis,node = heapq.heappop(heap)
        if distance[node]>dis:
            continue
        for next,w in graph[node]:
            if dis+w<distance[next]:
                distance[next] = dis+w
                heapq.heappush(heap,(distance[next],next))

    return distance[end]

ans = min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N),dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N))
print(ans if ans!=float("inf") else -1)
