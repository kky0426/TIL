from sys import stdin
from collections import defaultdict
import heapq


def dijkstar(s):
    distance = [float("inf")] * (n + 1)
    distance[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))

    while queue:
        dis, node = heapq.heappop(queue)
        if distance[node] < dis:
            continue

        for nex, w in graph[node]:
            if distance[nex] > dis + w:
                distance[nex] = dis + w
                heapq.heappush(queue, (distance[nex], nex))

    return distance

T = int(stdin.readline())

for _ in range(T):
    n,m,t = map(int,stdin.readline().split())
    s,g,h = map(int, stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(m):
        u,v,w = map(int, stdin.readline().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

    candidate = [int(stdin.readline()) for _ in range(t)]
    candidate.sort()
    S = dijkstar(s)
    G = dijkstar(g)
    H = dijkstar(h)
    for i in candidate:
        if S[i] == float("inf"):
            continue
        # s->g->h->i
        if S[i] == S[g]+G[h]+H[i]:
            print(i)
        # s->h->g->i
        elif S[i] == S[h]+H[g]+G[i]:
            print(i)






