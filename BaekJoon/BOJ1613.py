from sys import stdin

N,K = map(int,stdin.readline().split())

graph = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    s,e = map(int,stdin.readline().split())
    graph[s-1][e-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]: graph[i][j] = 1


S = int(stdin.readline())

for _ in range(S):
    s,e = map(int,stdin.readline().split())
    if graph[s-1][e-1]:
        print(-1)
    elif graph[e-1][s-1]:
        print(1)
    else:
        print(0)
