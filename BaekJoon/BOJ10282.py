from sys import stdin
from collections import defaultdict
import heapq


T = int(stdin.readline())

def dijkstra(start):
    distance = [float("inf") for _ in range(N+1)]
    distance[start] = 0

    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        dis,node = heapq.heappop(heap)
        for next,weight in graph[node]:
            if distance[next]>dis+weight:
                distance[next] = dis+weight
                heapq.heappush(heap,(distance[next],next))

    time=0
    count = 0
    for dis in distance:
        if dis!=float("inf"):
            time=max(time,dis)
            count+=1
    print(count,time)

for _ in range(T):
    N,D,C = map(int,stdin.readline().split())
    graph=defaultdict(list)

    for _ in range(D):
        u,v,w = map(int,stdin.readline().split())
        graph[v].append((u,w))

    dijkstra(C)
