from sys import stdin

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x= find(x)
    y = find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

N = int(stdin.readline())
M = int(stdin.readline())
parent = [i for i in range(N+1)]
graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]



for _ in range(M):
    x,y = map(int,stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
    union(x,y)

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j]=graph[i][k]+graph[k][j]


group = [[-1,float("inf")] for _ in range(N+1)]

for i in range(1,N+1):
    p = find(i)
    s = -1
    for j in range(1,N+1):
        if i==j:
            continue
        if p!=find(j):
            continue
        if graph[i][j] != float("inf"): s = max(s,graph[i][j])
    if group[p][1]>s:
        group[p][0] = i
        group[p][1] = s


ans = []
for i in range(1,N+1):
    if group[i][0]>0:
        ans.append(group[i][0])

print(len(ans))
ans.sort()
for a in ans: print(a)
