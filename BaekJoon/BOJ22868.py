from sys import stdin
from collections import deque,defaultdict

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for k,v in graph.items():
    v.sort()

s,e = map(int,stdin.readline().split())

def bfs(s,e):
    visit[s] = True
    queue = deque()
    queue.append((s,0))

    while queue:
        cur,dis = queue.popleft()
        if cur == e:
            return dis

        for n in graph[cur]:
            if not visit[n]:
                visit[n] = True
                pre[n] = cur
                queue.append((n,dis+1))


ans = 0
visit = [False]*(N+1)
pre = [-1]*(N+1)
ans+=bfs(s,e)

path = [e]
cur = e
while True:
    if pre[cur] == -1:
        break
    path.append(pre[cur])
    cur = pre[cur]

visit = [False]*(N+1)
for idx in path:
    visit[idx] = True
visit[s] = False
ans+=bfs(e,s)

print(ans)




















