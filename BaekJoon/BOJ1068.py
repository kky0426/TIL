from sys import stdin
from collections import deque,defaultdict

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
deleted = int(stdin.readline())

tree = defaultdict(list)
for i in range(N):
    if nums[i] == -1:
        root = i
        continue
    tree[nums[i]].append(i)

def bfs(root):
    count = 0
    queue = deque()
    queue.append(root)
    while queue:
        cur = queue.popleft()
        if cur == deleted:
            if len(tree[nums[cur]]) == 1:
                count+=1
            continue
        if cur not in tree:
            count+=1
            continue

        for next in tree[cur]:
            queue.append(next)

    return count

print(bfs(root))
