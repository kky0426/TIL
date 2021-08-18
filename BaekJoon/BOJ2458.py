from sys import stdin

N,M = map(int,stdin.readline().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]\

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u][v] = True

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

ans = 0
for i in range(1,N+1):
    count = 0
    for j in range(1,N+1):
        count+=graph[i][j] + graph[j][i]
    if count==N-1:
        ans+=1

print(ans)
