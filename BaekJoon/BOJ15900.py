from sys import stdin
from collections import defaultdict,deque


N = int(stdin.readline())
graph = defaultdict(list)
for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

ans = 0

def bfs(node):
    visit = [False]*(N+1)
    visit[node] = True
    queue = deque()
    queue.append((node,0))
    while queue:
        node,count = queue.popleft()
        if node!=1 and len(graph[node])==1 and count%2==1:
            global ans
            ans+=1
            continue

        for next in graph[node]:
            if not visit[next]:
                visit[next]=True
                queue.append((next,count+1))
bfs(1)

if ans%2 == 0:
    print("No")
else:
    print("Yes")
