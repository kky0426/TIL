from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

parent = [n for n in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x=find(x)
    y=find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    union(u,v)


com = find(1)
ans = 0
for i in range(2,N+1):
    if find(i) == com:
        ans+=1

print(ans)
