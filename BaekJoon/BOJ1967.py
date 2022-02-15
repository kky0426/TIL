from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())
graph = defaultdict(list)

for _ in range(N-1):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
ans = 0

visit = [False]*(N+1)
def dfs(node,parent):
    if visit[node]:
        return 0
    dis = 0
    visit[node] = True
    for n,w in graph[node]:
        if n == parent:
            continue
        cur = dfs(n,node)+w+dis
        global ans
        ans = max(ans,cur)
        dis = max(dis,cur-dis)
    return dis

dfs(1,-1)
print(ans)
