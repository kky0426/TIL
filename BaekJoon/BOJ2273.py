from sys import stdin

N,M = map(int,stdin.readline().split())

graph = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    graph[u][v] = True

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

flag = False
for i in range(1,N+1):
    if flag:
        break
    for j in range(1,N+1):
        if i == j: continue
        if graph[i][j] and graph[j][i]:
            flag = True
            break

if flag:
    print(-1)
else:
    for i in range(1,N+1):
        left = 1
        right = N
        for j in range(1,N+1):
            if graph[i][j]:
                right-=1
            if graph[j][i]:
                left+=1
        print(left,right)
