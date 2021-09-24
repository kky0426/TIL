from sys import stdin

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y


T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    nums = list(map(int,stdin.readline().split()))
    parent = [i for i in range(N+1)]
    ans = 0
    for  i in range(1,N+1):
        if find(i)==find(nums[i-1]):
            ans+=1
        union(i,nums[i-1])
    print(ans)
