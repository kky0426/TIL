from sys import stdin

N,M = map(int,stdin.readline().split())
ans = 0

parent = [i for i in range(N+1)]

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

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    union(u,v)

subject = list(map(int,stdin.readline().split()))

for i in range(N-1):
    if find(subject[i]) != find(subject[i+1]):
        ans+=1
print(ans)