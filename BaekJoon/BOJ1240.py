from sys import stdin
from collections import deque,defaultdict

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)

def get_distance(u,v):
    if u==v:
        return 0
    queue = deque()
    visit = [False]*(N+1)
    queue.append((u,0))
    visit[u] = True
    while queue:
        cur,count = queue.popleft()
        if cur == v:
            return count
        for next,dis in graph[cur]:
            if not visit[next]:
                visit[next]=True
                queue.append((next,count+dis))

for _ in range(N-1):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    print(get_distance(u,v))
