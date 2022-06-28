from sys import stdin
from collections import defaultdict,deque

N = int(stdin.readline())
degree = {}
graph = defaultdict(list)
total = set()
ans = []
for _ in range(N):
    u,v = stdin.readline().split()
    total.add(u)
    total.add(v)
    graph[u].append(v)
    graph[v].append(u)
    if not u in degree:
        degree[u]=0
    if not v in degree:
        degree[v]=0

    degree[v]+=1

queue = deque()
for k,v in degree.items():
    if v == 0:
        queue.append(k)

while queue:
    temp = []
    for _ in range(len(queue)):
        item = queue.popleft()
        temp.append(item)
        for nxt in graph[item]:
            degree[nxt]-=1
            if degree[nxt] == 0:
                queue.append(nxt)
    temp.sort()
    ans.extend(temp)

if len(total)!=len(ans):
    print(-1)
else:
    for word in ans:
        print(word)
