from sys import stdin
from collections import defaultdict

N,M,A,B,C = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

ans = float("inf")

visit = [False]*(N+1)
def dfs(node,cost,money):
    if node == B:
        global ans
        ans = min(ans,cost)
        return

    for n,w in graph[node]:
        if money-w >= 0 and not visit[n]:
            visit[n] = True
            dfs(n,max(cost,w),money-w)
            visit[n] = False

dfs(A,0,C)
print(ans if ans!=float("inf") else -1)
