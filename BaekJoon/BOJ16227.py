from sys import stdin
from collections import defaultdict
import heapq

N,K = map(int,stdin.readline().split())

graph = defaultdict(list)
for _ in range(K):
    u,v,w = map(int,stdin.readline().split())
    graph[v].append((u,w))
    graph[u].append((v,w))


def dijkstra(start,end):
    distance = [[float("inf") for _ in range(101)] for _ in range(N+2)]
    queue = []
    heapq.heappush(queue,(0,start,100))
    distance[start][100] = 0
    while queue:
        dis,node,remain = heapq.heappop(queue)
        if distance[node][remain] < dis:
            continue
        for n,w in graph[node]:
            if w>100:
                continue
            if remain>=w:
                if distance[n][remain-w]>dis+w:
                    distance[n][remain-w] = dis+w
                    heapq.heappush(queue,(dis+w,n,remain-w))
            else:
                if distance[n][100-w]>dis+w+5:
                    distance[n][100-w] = dis+w+5
                    heapq.heappush(queue,(dis+w+5,n,100-w))
    return min(distance[end])
print(dijkstra(0,N+1))