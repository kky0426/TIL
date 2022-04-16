from sys import stdin
from collections import defaultdict
import heapq

N,M  = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w*2))
    graph[v].append((u,w*2))

def fox():
    distance = [float("inf")]*(N+1)
    distance[1] = 0
    queue = []
    heapq.heappush(queue,(0,1))

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if distance[n]>dis+w:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))

    return distance

def wolf():
    distance = [[float("inf") for _ in range(2)] for _ in range(N+1)]
    distance[1][1] = 0
    queue = []
    heapq.heappush(queue,(0,1,0))

    while queue:
        dis,node,flag = heapq.heappop(queue)

        if distance[node][1-flag] < dis:
            continue

        for n,w in graph[node]:
            if flag == 0:
                if distance[n][0] > distance[node][1] + w//2:
                    distance[n][0] = distance[node][1] + w//2
                    heapq.heappush(queue,(distance[n][0],n,1-flag))
            else:
                if distance[n][1] > distance[node][0] + w*2:
                    distance[n][1] = distance[node][0]+w*2
                    heapq.heappush(queue,(distance[n][1],n,1-flag))

    return distance


fox_dis = fox()
wolf_dis = wolf()
ans = 0

for i in range(2,N+1):
    if fox_dis[i] < min(wolf_dis[i]):
        ans+=1
print(ans)