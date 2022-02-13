from sys import stdin

N,M = map(int,stdin.readline().split())

graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k]+graph[k][j]<graph[i][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

for _ in range(M):
    s,e,t = map(int,stdin.readline().split())
    if graph[s-1][e-1] <=t:
        print("Enjoy other party")
    else:
        print("Stay here")
