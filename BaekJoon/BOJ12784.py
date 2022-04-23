from sys import stdin
from collections import defaultdict


def dfs(node,parent):
    visit[node] = True
    cost = 0
    parent_cost = 0
    for child,w in graph[node]:
        if child == parent:
            parent_cost = w
            continue
        if not visit[child]:
            cost+=dfs(child,node)

    if len(graph[node]) == 1:
        return parent_cost

    if cost == 0:
        return 0
    else:
        return min(cost,parent_cost)

T = int(stdin.readline())

for _ in range(T):
    N,M = map(int,stdin.readline().split())
    graph = defaultdict(list)
    visit = [False]*(N+1)
    for _ in range(M):
        u,v,w = map(int,stdin.readline().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

    ans = 0
    for child,w in graph[1]:
        ans+=dfs(child,1)
    print(ans)


