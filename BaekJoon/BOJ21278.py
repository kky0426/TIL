from sys import stdin

N,M = map(int,stdin.readline().split())

graph  = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1,N+1):
    graph[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

ans = float("inf")
p1,p2 = 0,0

for i in range(1,N+1):
    for j in range(1,N+1):
        dis = 0
        for k in range(1,N+1):
            dis+=min(graph[k][i],graph[k][j])

        if ans>dis:
            ans = dis
            p1 = i
            p2 = j

print(p1,p2,ans*2)