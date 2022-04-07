from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())
tree = [[] for _ in range(N+1)]
visit = [False]*(N+1)
dp = [[0 for _ in range(2)] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(node):
    visit[node] = True
    dp[node][1] = 1
    for child in tree[node]:
        if not visit[child]:
            dfs(child)
            dp[node][0]+=dp[child][1]
            dp[node][1]+=min(dp[child][0],dp[child][1])

dfs(1)
print(min(dp[1]))
