from sys import stdin
from collections import deque

N,K = map(int,stdin.readline().split())

nums = [int(stdin.readline()) for _ in range(N)]

def bfs():
    queue = deque()
    count = [0]*(N+1)
    queue.append(0)

    while queue:
        node = queue.popleft()
        if node == K:
            return count[node]

        nxt = nums[node]
        if count[nxt] == 0:
            count[nxt] = count[node]+1
            queue.append(nxt)

    return -1

print(bfs())