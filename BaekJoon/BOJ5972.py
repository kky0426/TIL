from sys import stdin
from collections import defaultdict
import heapq

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))


def dijkstra(start):
    distance = [float("inf")]*(N+1)
    distance[start] = 0
    heap = [(0,start)]
    while heap:
        weight,cur = heapq.heappop(heap)
        if distance[cur]<weight:
            continue

        for u,w in graph[cur]:
            dis = weight+w
            if dis<distance[u]:
                distance[u] = dis
                heapq.heappush(heap,(dis,u))

    return distance[N]

print(dijkstra(1))
