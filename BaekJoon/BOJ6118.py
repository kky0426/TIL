from sys import stdin
from collections import defaultdict
from collections import deque

N,M = map(int,stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

distance = [float("inf")]*(N+1)

def dijkstra(start):
    distance[start] = 0
    queue = deque()
    queue.append((0,start))

    while queue:
        dis,node = queue.popleft()

        if distance[node]<dis:
            continue

        for next in graph[node]:
            if dis+1 < distance[next]:
                distance[next] = dis+1
                queue.append((distance[next],next))

dijkstra(1)
m = max(distance[1:])
ans = 0
count=0
for i in range(N,0,-1):
    if distance[i]==m:
        ans=i
        count+=1
print(ans,m,count)
