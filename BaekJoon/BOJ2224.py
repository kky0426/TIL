from sys import stdin

N = int(stdin.readline())


graph = [[False for _ in range(58)] for _ in range(58)]

ans = 0

for _ in range(N):
    u,v = stdin.readline().replace(" ","").rstrip().split("=>")
    u = ord(u)-65
    v = ord(v)-65
    if u == v or graph[u][v]:
        continue
    graph[u][v] = True
    ans+=1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i == j or graph[i][j]:
                continue
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True
                ans+=1
print(ans)
for i in range(58):
    for j in range(58):
        if graph[i][j]:
            print(chr(i+65)+" => "+chr(j+65))
