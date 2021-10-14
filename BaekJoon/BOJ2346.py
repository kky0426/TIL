from sys import stdin
from collections import deque

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))
queue = deque([i for i in range(N)])
ans = []
idx = 0
while queue:
    count = nums[idx]
    if idx == queue[0]:
        ans.append(queue.popleft()+1)
    else:
        ans.append(queue.pop()+1)
    if count>0:
        for _ in range(count-1):
            if queue:
                queue.append(queue.popleft())
        if queue: idx = queue[0]
    else:
        for _ in range(-count-1):
            if queue:
                queue.appendleft(queue.pop())
        if queue: idx = queue[-1]
print(*ans)
