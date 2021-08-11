from sys import stdin
from collections import deque
from collections import defaultdict

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)
visit = [0]*(N+1)

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if visit[next]==0:
                queue.append(next)
                visit[next]=1

ans=0
for i in range(1,N+1):
    if visit[i]==0:
        bfs(i)
        ans+=1

print(ans)
