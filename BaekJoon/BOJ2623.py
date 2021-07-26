from sys import stdin
from collections import deque
ans=[]
N,M = map(int,stdin.readline().split())

graph=[[]for _ in range(N+1)]
degree = [0]*(N+1)

for _ in range(M):
    s = list(map(int,stdin.readline().rstrip().split()))[1:]
    for i in range(len(s)-1):
        graph[s[i]].append(s[i+1])
        degree[s[i+1]]+=1

queue=deque()

for i in range(1,N+1):
    if degree[i]==0:
        queue.append(i)

while queue:
    node = queue.popleft()
    ans.append(node)
    for d in graph[node]:
        degree[d]-=1
        if degree[d]==0:
            queue.append(d)

if len(ans)==N:
    for p in ans:
        print(p)
else:
    print(0)
