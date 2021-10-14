from sys import stdin
from collections import deque,defaultdict

N,M,V = map(int,stdin.readline().split())

graph = defaultdict(list)
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

def bfs(start):
    visit = [False]*(N+1)
    visit[start] = True
    queue = deque()
    queue.append(start)
    print(start,end=" ")
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visit[next]:
                visit[next]=True
                queue.append(next)
                print(next,end=" ")


visited = [False]*(N+1)
def dfs(start,visited):
    print(start,end=" ")
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(next,visited)

dfs(V,visited)
print()
bfs(V)
