from sys import stdin
from collections import defaultdict

N,M = map(int,stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))

distance = [float("inf")]*(N+1)
distance[1] = 0

def bellman():
    for i in range(N):
        for node in range(1,N+1):
            for next,time in graph[node]:
                if distance[next]>distance[node]+time:
                    distance[next] = distance[node]+time
                    if i==N-1: return True
    return False

if bellman():
    print(-1)
else:
    for ans in distance[2:]:
        print(ans if ans!=float("inf") else -1)
