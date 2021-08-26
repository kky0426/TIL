from sys import stdin

N = int(stdin.readline())

M = int(stdin.readline())

graph = [[float("inf") for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s,e,w = map(int,stdin.readline().split())
    graph[s-1][e-1] = min(graph[s-1][e-1],w)


for k in range(N):
    for i in range(N):
        for j in range(N):
            if i!=j and graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(N):
    for j in range(N):
        print(graph[i][j] if graph[i][j]!=float("inf") else 0,end=" ")
    print()
