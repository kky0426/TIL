from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())
graph = defaultdict(list)

for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False]*(N+1)
dp = [[0,0] for _ in range(N+1)]

def dfs(cur):
    visit[cur] = True
    dp[cur][1] = 1
    for node in graph[cur]:
        if not visit[node]:
            dfs(node)
            dp[cur][0]+=dp[node][1]
            dp[cur][1]+=min(dp[node][0],dp[node][1])

dfs(1)
print(min(dp[1]))