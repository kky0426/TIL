from sys import stdin
from collections import defaultdict
import heapq

N = int(stdin.readline())
M = int(stdin.readline())

graph=defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

ans=0
heap = [(0,1)]
visit = set()
while heap:
    w,com = heapq.heappop(heap)
    if com not in visit:
        ans+=w
        visit.add(com)
        for next in graph[com]:
            heapq.heappush(heap,next)

print(ans)
\
