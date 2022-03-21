from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N,M = map(int,stdin.readline().split())

graph = defaultdict(list)
praise = [0]*(N+1)

line = list(map(int,stdin.readline().split()))

for i in range(1,N):
    graph[line[i]].append(i+1)

def dfs(node):
    for n in graph[node]:
        praise[n]+=praise[node]
        dfs(n)

for _ in range(M):
    i,w = map(int,stdin.readline().split())
    praise[i]+=w

dfs(1)

print(*praise[1:])