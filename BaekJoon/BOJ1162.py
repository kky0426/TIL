from sys import stdin
from collections import defaultdict
import heapq

N,M,K = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra():
    distance = [[float("inf") for _ in range(K+1)] for _ in range(N+1)]
    distance[1][0] = 0
    queue = []
    heapq.heappush(queue,(0,1,0))

    while queue:
        dis,node,count = heapq.heappop(queue)
        if distance[node][count] < dis:
            continue

        for n,w in graph[node]:
            if distance[n][count] > dis+w:
                distance[n][count] = dis+w
                heapq.heappush(queue,(distance[n][count],n,count))

            if count<K and distance[n][count+1] > dis:
                distance[n][count+1] = dis
                heapq.heappush(queue,(distance[n][count+1],n,count+1))

    return min(distance[N])

print(dijkstra())