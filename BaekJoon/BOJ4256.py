from sys import stdin

T = int(stdin.readline())

def solve(preorder,inorder):
    if len(preorder) == 0:
        return

    if len(preorder) == 1:
        ans.append(preorder[0])
        return

    root = preorder[0]
    idx = inorder.index(root)
    solve(preorder[1:idx+1],inorder[:idx])
    solve(preorder[idx+1:],inorder[idx+1:])
    ans.append(root)

for _ in range(T):
    N = int(stdin.readline())
    ans = []
    preorder = list(map(int,stdin.readline().split()))
    inorder = list(map(int,stdin.readline().split()))
    solve(preorder,inorder)
    print(*ans)
