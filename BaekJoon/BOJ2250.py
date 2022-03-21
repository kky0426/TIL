from sys import stdin

N = int(stdin.readline())
tree = [[-1,-1] for _ in range(N+1)]
degree = [0]*(N+1)
for _ in range(N):
    n,l,r = map(int,stdin.readline().split())
    tree[n][0] = l
    tree[n][1] = r
    degree[n]+=1
    if l != -1:
        degree[l]+=1
    if r != -1:
        degree[r]+=1

row = [[] for _ in range(N+1)]

num = 1

def dfs(node,depth):
    if tree[node][0]!=-1:
        dfs(tree[node][0],depth+1)
    global num
    row[depth].append(num)
    num+=1

    if tree[node][1]!=-1:
        dfs(tree[node][1],depth+1)

root = 0

for i in range(1,N+1):
    if degree[i] == 1:
        root = i
        break
dfs(root,1)

depth = 1
ans = max(row[1])-min(row[1])+1
for i in range(2,N+1):
    if row[i]:
        mx = max(row[i])
        mi = min(row[i])
        if ans<mx-mi+1:
            ans = mx-mi+1
            depth = i

print(depth,ans)