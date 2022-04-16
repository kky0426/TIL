from sys import stdin
from collections import defaultdict
import heapq

N = int(stdin.readline())
graph = defaultdict(list)

for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dijkstar(start):
    distance = [float("inf")]*(N+1)
    distance[start] = 0
    queue = [(0,start)]
    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue
        for child in graph[node]:
            if distance[child]>dis+1:
                distance[child] = dis+1
                heapq.heappush(queue,(distance[child],child))
    idx = 0
    max_dis = 0
    for i in range(1,N+1):
        if max_dis<distance[i]:
            max_dis = distance[i]
            idx = i

    return idx,max_dis

idx,dis = dijkstar(1)
_,ans = dijkstar(idx)

print((1+ans)//2)