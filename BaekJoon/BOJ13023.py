from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N,M =map(int,stdin.readline().split())
graph = defaultdict(list)
ans = 0
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node,count):
    global ans
    visit[node] = 1
    if count == 4:
        ans = 1
        return
    if ans == 1:
        return

    for next in graph[node]:
        if visit[next]==0:
            dfs(next,count+1)
            visit[next]=0

visit = [0]*N
for i in range(N):
    dfs(i,0)
    visit[i] = 0
print(ans)
