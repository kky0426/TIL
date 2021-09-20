from sys import stdin
from collections import defaultdict
import heapq

N = int(stdin.readline())
M = int(stdin.readline())

graph = defaultdict(list)
for _ in range(M):
   u,v,w = map(int,stdin.readline().split())
   graph[u].append((v,w))

src,des = map(int,stdin.readline().split())
distance = [float("inf")]*(N+1)
path = [0]*(N+1)
ans = []
def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))

    while queue:
        dis,node = heapq.heappop(queue)
        if dis>distance[node]:
            continue

        for next,w in graph[node]:
            if dis+w<distance[next]:
                distance[next] = dis+w
                heapq.heappush(queue,(distance[next],next))
                path[next] = node

dijkstra(src)

ans = [des]
temp=des
while path[temp]!=0:
    ans.append(path[temp])
    temp = path[temp]


print(distance[des])
print(len(ans))
print(" ".join(map(str,reversed(ans))))
