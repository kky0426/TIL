from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

graph = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u-1][v-1] = True
    #graph[v-1][u-1] = True

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

for i in range(N):
    count = 1
    for j in range(N):
        if graph[i][j] or graph[j][i]:
            count+=1
    print(N-count)
