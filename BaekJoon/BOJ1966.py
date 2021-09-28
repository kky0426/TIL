from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    N,M = map(int,stdin.readline().split())

    priority = list(map(int,stdin.readline().split()))
    count = [0]*10

    queue = deque()
    for i in range(N):
        queue.append((priority[i],i))
        count[priority[i]]+=1

    ans = 1
    while queue:
        p,idx = queue[0]
        if sum(count[p+1:]) == 0:
            _,idx = queue.popleft()
            if idx == M:
                print(ans)
                break
            ans+=1
            count[p]-=1

        else:
            queue.append(queue.popleft())
