from sys import stdin

N = int(stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int,stdin.readline().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for line in graph:
    print(" ".join(map(str,line)))
