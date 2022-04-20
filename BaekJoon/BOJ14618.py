from sys import stdin
from collections import defaultdict
import heapq

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)
J = int(stdin.readline())
K = int(stdin.readline())

A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def diskstra(start):
    distance = [float("inf")] *(N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))

    while queue:
        dis,node = heapq.heappop(queue)
        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if distance[n] > dis+w:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))

    return distance

distance = diskstra(J)
dis = float("inf")
idx = 0

for i in range(1,N+1):
    if i == J:
        continue

    if dis>distance[i]:
        dis = distance[i]
        idx = i

dis = float("inf")
ans = -1
for num in A:
    if dis>distance[num]:
        dis = distance[num]
        ans = "A"

for num in B:
    if dis>distance[num]:
        dis = distance[num]
        ans = 'B'

if ans == -1:
    print(ans)
else:
    print(ans)
    print(dis)