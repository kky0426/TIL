from sys import stdin

V,E = map(int,stdin.readline().split())

graph = [[float("inf") for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,stdin.readline().split())
    graph[u][v] = w


for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


ans = float("inf")
for i in range(1,V+1):
    ans = min(ans,graph[i][i])

print(ans if ans!=float("inf") else -1)
