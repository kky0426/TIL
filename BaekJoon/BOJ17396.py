from sys import stdin
import heapq
from collections import defaultdict

N,M = map(int,stdin.readline().split())

sight = list(map(int,stdin.readline().split()))
graph = defaultdict(list)
for _ in range(M):
    a,b,t = map(int,stdin.readline().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

def dijkstra():
    distance = [float("inf")]*N
    queue =[]
    distance[0] = 0
    heapq.heappush(queue,(0,0))

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if n!=N-1 and sight[n] == 1:
                continue
            if distance[n]>dis+w:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))
    return distance[N-1]

ans = dijkstra()
print(ans if ans!=float("inf") else -1)
