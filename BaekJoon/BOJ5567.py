from sys import stdin
from collections import defaultdict


graph = defaultdict(list)

N = int(stdin.readline())
M = int(stdin.readline())

for _ in range(M):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = set()
temp=[]
for node in graph[1]:
    ans.add(node)
    temp.append(node)

for i in temp:
    for node in graph[i]:
        ans.add(node)
ans.discard(1)
print(len(ans))
