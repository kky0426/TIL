from sys import stdin

N = int(stdin.readline())

graph = [list(map(int,stdin.readline().rstrip().replace("N",'0').replace("Y",'1'))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = float("inf")

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
ans = 0
for i in range(N):
    count = 0
    for j in range(N):
        if i==j: continue
        if graph[i][j]<=2:
            count+=1
    ans = max(ans,count)
print(ans)
