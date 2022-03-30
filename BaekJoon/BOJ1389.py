from sys import stdin

N,M = map(int,stdin.readline().split())

graph = [[float("inf") for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

ans = 0
max_num =  float("inf")

for i in range(N):
    s = sum(graph[i])
    if s<max_num:
        ans = i
        max_num = s

print(ans+1)