from sys import stdin
import heapq
from collections import defaultdict

def dijkstra(start):
    distance = [float("inf")]*(N+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))
    while heap:
        dis,node = heapq.heappop(heap)
        if dis>distance[node]:
            continue

        for next,w in graph[node]:
            if dis+w<distance[next]:
                distance[next] = dis+w
                heapq.heappush(heap,(distance[next],next))

    flag = True
    for i in range(1,N+1):
        if distance[i] == K:
            print(i)
            flag = False
    if flag: print(-1)

N,M,K,X = map(int,stdin.readline().split())

graph = defaultdict(list)
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append((v,1))

dijkstra(X)
