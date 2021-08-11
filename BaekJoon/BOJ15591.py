from sys import stdin
from collections import defaultdict
from collections import deque

N,Q = map(int,stdin.readline().split())
graph = defaultdict(list)
for _ in range(N-1):
    p,q,r = map(int,stdin.readline().split())
    graph[p].append((q,r))
    graph[q].append((p,r))


def bfs(start,K):
    queue = deque()
    queue.append((start,float('inf')))
    visit = set()
    visit.add(start)
    ans = 0
    while queue:
        node,usado = queue.popleft()
        for next,v in graph[node]:
            if next not in visit:
                min_usado = min(usado,v)
                visit.add(next)
                queue.append((next,min_usado))
                if min_usado>=K: ans+=1
    return ans

for _ in range(Q):
    k,v =map(int,stdin.readline().split())
    print(bfs(v,k))
