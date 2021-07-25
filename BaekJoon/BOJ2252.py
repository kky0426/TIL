from sys import stdin

from collections import deque

N,M = map(int,stdin.readline().split())
graph=[[] for _ in range(N+1)]
degree=[0]*(N+1)

for _ in range(M):
    a,b=map(int,stdin.readline().split())
    degree[b]+=1
    graph[a].append(b)

queue=deque()
for i in range(1,N+1):
    if degree[i]==0:
        queue.append(i)

while queue:
    node=queue.popleft()
    print(node,end=' ')
    for d in graph[node]:
        degree[d]-=1
        if degree[d]==0:
            queue.append(d)
