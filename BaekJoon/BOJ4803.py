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
        parent[y]=x
    else:
        parent[x]=y

case = 1
while True:
    n,m = map(int,stdin.readline().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    cycle = [False for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,stdin.readline().split())
        pu = find(u)
        pv = find(v)
        if pu!=pv:
            if cycle[pu] or cycle[pv]:
                cycle[pu] = True
                cycle[pv] = True
            union(u,v)
        else:
            cycle[pu] = True
    ans = 0
    tree = set()
    for i in range(1,n+1):
        p = find(i)
        if cycle[p]:continue
        if p not in tree:
            ans+=1
            tree.add(p)

    if ans == 0:
        print("Case {}: No trees.".format(case))
    elif ans == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case,ans))

    case+=1