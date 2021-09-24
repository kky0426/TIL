from sys import stdin
import heapq
from collections import defaultdict

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

path = [0]*(N+1)

def dijkstra(start):
    distance = [float("inf")]*(N+1)
    distance[start] = 0
    heap=[]
    ans = []
    heapq.heappush(heap,(0,start))
    while heap:
        dis,node = heapq.heappop(heap)

        if distance[node]<dis:
            continue
        for next,w in graph[node]:
            if dis+w<distance[next]:
                distance[next] = dis+w
                heapq.heappush(heap,(distance[next],next))
                path[next] = node


dijkstra(1)
print(N-1)
for i in range(2,N+1):
    print("{} {}".format(i,path[i]))
