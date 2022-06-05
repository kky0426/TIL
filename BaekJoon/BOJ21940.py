from sys import stdin

N,M = map(int,stdin.readline().split())

graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    u,v,w = map(int,stdin.readline().split())
    graph[u][v] = w

K = int(stdin.readline())
city = list(map(int,stdin.readline().split()))

max_dis = float("inf")
ans = []

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j]> graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

for i in range(1,N+1):
    dis = 0
    for c in city:
        dis=max(dis,graph[i][c]+graph[c][i])
    if dis<max_dis:
        max_dis = dis
        ans = [i]
    elif dis == max_dis:
        ans.append(i)
print(*ans)

