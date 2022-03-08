from sys import stdin

N,M = map(int,stdin.readline().split())

INF = float("inf")
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u][v] = w
    graph[v][u] = w

ans = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            ans[i][j] = j+1
        else:
            ans[i][j] = "-"


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
                ans[i-1][j-1] = ans[i-1][k-1]

for arr in ans:
    print(*arr)