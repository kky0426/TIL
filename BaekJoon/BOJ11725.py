from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline())

tree = defaultdict(list)
parent = [0]*(N+1)
visit = [False]*(N+1)

def dfs(node):
    visit[node] = True
    for n in tree[node]:
        if not visit[n]:
            parent[n] = node
            dfs(n)

for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

visit[1] = True
dfs(1)

for num in parent[2:]:
    print(num)