from sys import stdin
from collections import defaultdict
import heapq

V,E = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(E):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

visit=set()
heap=[]
heap.append((0,1))

ans=0

while heap:
    w,node = heapq.heappop(heap)
    if node not in visit:
        visit.add(node)
        ans+=w
        for next in graph[node]:
            heapq.heappush(heap,next)
            
print(ans)
