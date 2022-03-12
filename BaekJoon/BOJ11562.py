from sys import stdin

N,M = map(int,stdin.readline().split())

graph = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    u,v,b = map(int,stdin.readline().split())
    if b == 0:
        graph[u-1][v-1] = 0
        graph[v-1][u-1] = 1
    else:
        graph[u-1][v-1] = 0
        graph[v-1][u-1] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

K = int(stdin.readline())
for _ in range(K):
    u,v = map(int,stdin.readline().split())
    print(graph[u-1][v-1])
