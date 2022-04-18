from sys import stdin

H = int(stdin.readline())

tree = [0,0]+list(map(int,stdin.readline().split()))

ans = 0
def dfs(idx,depth):
    global ans
    if depth == H:
        ans+=tree[idx]
        return tree[idx]

    left = dfs(idx*2,depth+1)
    right = dfs(idx*2+1,depth+1)
    diff = abs(left-right)
    ans+=tree[idx]+diff
    return tree[idx]+max(left,right)

dfs(1,0)
print(ans)