from sys import stdin
from collections import defaultdict

visit = [False]*10001
graph = defaultdict(list)

while True:
    try:
        u,v,w = map(int,stdin.readline().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    except:
        break

ans = 0
idx = 0
def dfs(node,cost):
    for n,w in graph[node]:
        if visit[n]:
            continue
        visit[n] = True
        dis = cost+w
        global ans,idx
        if dis>ans:
            ans = dis
            idx = n
        dfs(n,dis)

visit[1] = True
dfs(1,0)
ans = 0
visit = [False]*10001
visit[idx] = True
dfs(idx,0)
print(ans)
