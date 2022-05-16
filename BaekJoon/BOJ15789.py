from sys import stdin

N,M = map(int,stdin.readline().split())

parent = [i for i in range(N+1)]
power = [1]*(N+1)
idxs = [i for i in range(N+1)]
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

    if x==y:
        return
    parent[y] = x
    power[x]+=power[y]
    power[y]=power[x]

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    union(u,v)

C,H,K = map(int,stdin.readline().split())

count = 0
idxs.sort(key=lambda x:power[x],reverse=True)
for idx in idxs:
    if find(idx) == C or find(idx) == H or idx == 0:
        continue
    if count>=K:
        break
    if find(C) != find(idx):
        union(C,idx)
        count+=1

print(power[C])
