from sys import stdin

N,M = map(int,stdin.readline().split())

warps = [list(map(int,stdin.readline().split())) for _ in range(M)]
ext = list(map(int,stdin.readline().split()))

for i in range(N):
    warps.append([0,i+1,ext[i]])

parent = [i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        parent[x] = temp
        return temp

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

warps.sort(key=lambda x:x[2])

edge = 0
ans = 0
for u,v,w in warps:
    if find(u) != find(v):
        union(u,v)
        ans+=w
        edge+=1
    if edge == N:
        break

print(ans)
