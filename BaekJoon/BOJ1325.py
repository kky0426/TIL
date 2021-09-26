from sys import stdin
from collections import defaultdict
from collections import deque

graph = defaultdict(list)

N,M = map(int,stdin.readline().split())
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[v].append(u)


def bfs(node):
    visit = [False]*(N+1)
    queue = deque()
    visit[node]=True
    queue.append(node)
    count = 0
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if visit[next]:
                continue
            count+=1
            visit[next]=True
            queue.append(next)
    return count

ans = [bfs(i) for i in range(1,N+1)]
m = max(ans)

for i in range(N):
    if ans[i] == m:
        print(i+1,end=" ")
