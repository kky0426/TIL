from sys import stdin
from collections import deque

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

T = int(stdin.readline())

for _ in range(T):
    R,C = map(int,stdin.readline().split())
    parent = [i for i in range(R*C)]
    queue = []

    for i in range(R):
        line = list(map(int,stdin.readline().split()))
        for j in range(len(line)):
            queue.append((line[j],i*C+j,i*C+j+1))

    for i in range(R-1):
        line = list(map(int,stdin.readline().split()))
        for j in range(len(line)):
            queue.append((line[j],i*C+j,i*C+j+C))
    ans = 0
    count = 0
    queue.sort(key=lambda x:x[0])
    queue = deque(queue)
    while queue:
        w,u,v = queue.popleft()
        if find(u)!=find(v):
           ans+=w
           count+=1
           union(u,v)

        if count == R*C-1:
            break
    print(ans)