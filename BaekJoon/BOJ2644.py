from sys import stdin
from collections import deque,defaultdict

N = int(stdin.readline())
graph = defaultdict(list)
x,y = map(int,stdin.readline().split())
M = int(stdin.readline())

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def  bfs(x,y):
    visit = [False]*(N+1)
    visit[x]=True
    queue = deque()
    queue.append((x,0))

    while queue:
        cur,count = queue.popleft()
        if cur == y:
            return count

        for n in graph[cur]:
            if not visit[n]:
                visit[n]=True
                queue.append((n,count+1))

    return -1

print(bfs(x,y))
