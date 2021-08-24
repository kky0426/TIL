from sys import stdin
from collections import defaultdict

def find(x):
    if x==parent[x]:
        return x
    else:
        return find(parent[x])

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

while True:
    M,N = map(int,stdin.readline().split())

    if M==0 and N==0: break
    
    parent = [n for n in range(M)]
    graph=defaultdict(list)
    house = []
    for _ in range(N):
        x,y,z = map(int,stdin.readline().split())
        house.append((x,y,z))
    house.sort(key=lambda x:x[2])

    ans = 0
    for x,y,z in house:
        if find(x)!=find(y):
            union(x,y)
        else:
            ans+=z
    print(ans)
