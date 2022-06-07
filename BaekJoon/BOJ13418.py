from sys import stdin

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x] = temp
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

N,M = map(int,stdin.readline().split())
parent = [i for i in range(N+1)]

graph = [list(map(int,stdin.readline().split())) for _ in range(M+1)]
graph.sort(key=lambda x:x[2])
max_ans = 0
count = 0
for u,v,w in graph:
    if find(u)!=find(v):
        union(u,v)
        if w == 0:
            max_ans+=1
            count+=1
    if count == N:
        break

parent = [i for i in range(N+1)]
graph.sort(key=lambda x:x[2],reverse=True)
min_ans = 0
count = 0
for u,v,w, in graph:
    if find(u)!=find(v):
        union(u,v)
        if w == 0:
            min_ans+=1
            count+=1
    if count == N:
        break
print(max_ans**2-min_ans**2)