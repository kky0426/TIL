from sys import stdin
from collections import defaultdict
T = int(stdin.readline())

def bellman(graph,start,N):
    distance = [INF]*(N+1)
    distance[start]=0

    for i in range(N):
        for v in range(1,N+1):
            for node,time in graph[v]:
                if distance[node]>distance[v]+time:
                    distance[node] = distance[v]+time
                    if i==N-1: return True
    return False

for _ in range(T):
    N,M,W = map(int,stdin.readline().split())
    INF = 2000000000

    graph = defaultdict(list)

    for _ in range(M):
        s,e,t = map(int,stdin.readline().split())
        graph[s].append((e,t))
        graph[e].append((s,t))

    for _ in range(W):
        s, e, t = map(int, stdin.readline().split())
        graph[s].append((e, -t))

    print("YES" if bellman(graph,1,N) else "NO")
