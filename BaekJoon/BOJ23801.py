from sys import stdin
from collections import defaultdict
import heapq

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

x,z = map(int,stdin.readline().split())
P = int(stdin.readline())
spot = list(map(int,stdin.readline().split()))

def dijkstar(start):
    distance = [float("inf")]*(N+1)
    distance[start] = 0
    queue = [(0,start)]

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if distance[n]>dis+w:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))

    return distance

src = dijkstar(x)
des = dijkstar(z)

ans = float("inf")

for y in spot:
    ans = min(ans,src[y]+des[y])

print(ans if ans!=float("inf") else -1)

