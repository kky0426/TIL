from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
people = list(map(int,stdin.readline().split()))

graph = defaultdict(list)
for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dp = [[0 for _ in range(2)] for _ in range(N)]
visit = [False]*N

def dfs(node):
    visit[node] = True
    dp[node][1] = people[node]

    for n in graph[node]:
        if not visit[n]:
            dfs(n)
            dp[node][0]+=max(dp[n][1],dp[n][0])
            dp[node][1]+=dp[n][0]

dfs(0)
print(max(dp[0]))
