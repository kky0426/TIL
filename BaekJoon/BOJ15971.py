from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N,start,end = map(int,stdin.readline().split())

graph = defaultdict(list)

for _ in range(N-1):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

visit = [False]*(N+1)

ans = 0

def dfs(node,dis,max_dis):
    if node == end:
        global ans
        ans = dis-max_dis
        return


    visit[node] = True

    for n,w in graph[node]:
        if not visit[n]:
            dfs(n,dis+w,max(w,max_dis))

dfs(start,0,0)
print(ans)
