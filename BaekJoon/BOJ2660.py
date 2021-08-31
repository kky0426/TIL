from sys import stdin


N = int(stdin.readline())

graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]

while True:
    u,v = map(int,stdin.readline().split())
    if u==-1 and v==-1:
        break
    graph[u][v] = 1
    graph[v][u] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                graph[i][j] = 0
                break
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

candidate = []
ans = float("inf")
for people in graph:
    ans = min(ans,max(people[1:]))

for i in range(1,N+1):
    if max(graph[i][1:]) == ans:
        candidate.append(i)
print(ans,len(candidate))
print(" ".join(map(str,candidate)))
