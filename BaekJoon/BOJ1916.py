from sys import stdin
import heapq
from collections import defaultdict

N = int(stdin.readline())
M = int(stdin.readline())
distance = [float("inf")] * (N+1)
graph = defaultdict(list)
for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((w,v))

start,end = map(int,stdin.readline().split())
heap = []
def dijkstar(start):
    distance[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        dis,cur = heapq.heappop(heap)

        if distance[cur]<dis:
            continue
        for w,next in graph[cur]:
            new_dis = dis+w
            if new_dis<distance[next]:
                distance[next] = new_dis
                heapq.heappush(heap,(new_dis,next))

dijkstar(start)
print(distance[end])
