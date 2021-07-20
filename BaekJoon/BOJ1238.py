from sys import stdin
from collections import defaultdict
import heapq
N,M,X = map(int,stdin.readline().split())

graph = defaultdict(list)
INF = float("inf")

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))



def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        cur_dis,cur_node = heapq.heappop(heap)

        if distance[cur_node]<cur_dis:
            continue

        for next,weight in graph[cur_node]:
            dis = cur_dis+weight
            if dis<distance[next]:
                distance[next] = dis
                heapq.heappush(heap,(dis,next))
    return distance

ans=0
for i in range(1,N+1):
    go=dijkstra(i)[X]
    back=dijkstra(X)[i]
    ans=max(ans,go+back)
print(ans)
