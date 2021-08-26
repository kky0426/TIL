from sys import stdin

N,M,R = map(int,stdin.readline().split())

items = list(map(int,stdin.readline().split()))

graph = [[float("inf") for _ in range(N)] for _ in range(N)]

for _ in range(R):
    s,e,w = map(int,stdin.readline().split())
    graph[s-1][e-1] = w
    graph[e-1][s-1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i!=j and graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = 0
for i in range(N):
    farming = items[i]
    for j in range(N):
        if graph[i][j]<=M:
            farming+=items[j]
    ans=max(ans,farming)
print(ans)
