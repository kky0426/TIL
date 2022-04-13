from sys import stdin

N = int(stdin.readline())

parent = [i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        temp = find(parent[x])
        return temp

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(N-2):
    u,v = map(int,stdin.readline().split())
    union(u,v)

flag = False
for i in range(1,N+1):
    if flag:
        break
    for j in range(1,N+1):
        if find(i)!=find(j):
            flag = True
            print(i,j)
            break
