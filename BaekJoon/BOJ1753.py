from sys import stdin
import heapq
from collections import defaultdict

V,E = map(int,stdin.readline().split())
start = int(input())
INF = float('inf')
distance = [INF]*(V+1)

heap = []
graph = defaultdict(list)

for _ in range(E):
    u,v,w=map(int,stdin.readline().split())
    graph[u].append((w,v))

def Dikstra(start):
    distance[start]=0
    heapq.heappush(heap,(0,start))

    while heap:
        wei,cur = heapq.heappop(heap)
        if distance[cur]<wei:
            continue

        for w,next in graph[cur]:
            dis = w+wei
            if dis<distance[next]:
                distance[next] = dis
                heapq.heappush(heap,(dis,next))

Dikstra(start)

for i in range(1,V+1):
    print("INF" if distance[i]==INF else distance[i])
