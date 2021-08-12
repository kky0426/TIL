from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

parent = [n for n in range(N)]

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

for i in range(N):
    line = list(map(int,stdin.readline().split()))
    for j in range(N):
        if line[j] == 1:
            union(i,j)

trip = list(map(int,stdin.readline().split()))

flag = True

for i in range(1,M):
    if find(trip[i-1]-1)!=find(trip[i]-1):
        flag=False
        break

print("YES" if flag else "NO")
