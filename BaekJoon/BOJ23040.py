from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x] = temp
        return temp

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    parent[y] = x
    count[x]+=count[y]
    count[y]=count[x]

N = int(stdin.readline())

graph = defaultdict(list)

for _ in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

color = [0]+list(stdin.readline().rstrip())

parent = [i for i in range(N+1)]
count = [1]*(N+1)

for i in range(1,N+1):
    if color[i] == 'B':
        continue
    for n in graph[i]:
        if color[n] == 'R':
            union(i,n)

ans = 0
for i in range(1,N+1):
    if color[i] == 'B':
       for n in graph[i]:
            if color[n] == 'R':
                ans+=count[find(n)]

print(ans)

