from sys import stdin
from collections import defaultdict,deque

N,M = map(int,stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    visit = [-1 for _ in range(N+1)]
    queue = deque()
    queue.append((1,0))
    while queue:
        node,dis = queue.popleft()
        if visit[node] == -1:
            visit[node] = dis
            for next_node in graph[node]:
                if visit[next_node] == -1:
                    queue.append((next_node,dis+1))
    return visit[1:]

Q = int(stdin.readline())

for _ in range(Q):
    a,i,j = map(int,stdin.readline().split())
    if a == 1:
        graph[i].append(j)
        graph[j].append(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)

    ans = bfs()
    print(*ans)