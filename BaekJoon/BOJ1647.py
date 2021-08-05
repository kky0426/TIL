from sys import stdin
from collections import defaultdict
import heapq

N,M = map(int,stdin.readline().split())

graph=defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((w,v))
    graph[v].append((w,u))
m=0
ans=0
heap = [(0,1)]
visit = set()
count = 0
while heap:
    if count == N:
        break
    w,com = heapq.heappop(heap)
    if com not in visit:
        ans+=w
        count+=1
        m=max(m,w)
        visit.add(com)
        for next in graph[com]:
            heapq.heappush(heap,next)

print(ans-m)
