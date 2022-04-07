from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N,R,Q = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False]*(N+1)
dp = [0]*(N+1)
def dfs(node):
    visit[node] = True
    dp[node] = 1
    for n in graph[node]:
        if not visit[n]:
            dfs(n)
            dp[node]+=dp[n]

dfs(R)

for _ in range(Q):
    u = int(stdin.readline())
    print(dp[u])
