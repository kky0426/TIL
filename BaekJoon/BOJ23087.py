from sys import stdin
from collections import defaultdict
import heapq


N,M,x,y = map(int,stdin.readline().split())
mod = 10**9+9
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))

distance = [float("inf")]*(N+1)
line = [0]*(N+1)
dp = [0]*(N+1)

def dijkstart(start):
    distance[start] = 0
    dp[start] = 1
    queue = []
    heapq.heappush(queue,(distance[start],start,0))

    while queue:
        dis,node,count = heapq.heappop(queue)

        if distance[node]<dis:
            continue

        for n,w in graph[node]:
            if dis+w < distance[n]:
                distance[n] = dis+w
                line[n] = count+1
                dp[n] = dp[node]
                heapq.heappush(queue,(distance[n],n,count+1))
            elif dis+w == distance[n] and count+1<line[n]:
                line[n] = count+1
                dp[n] = dp[node]
                heapq.heappush(queue,(distance[n],n,count+1))
            elif dis+w == distance[n] and count+1 == line[n]:
                dp[n]+=dp[node]
                dp[n]%=mod


dijkstart(x)
if distance[y] == float("inf"):
    print(-1)
else:
    print(distance[y])
    print(line[y])
    print(dp[y])

