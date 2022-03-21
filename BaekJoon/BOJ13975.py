from sys import stdin
import heapq

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    queue = list(map(int,stdin.readline().split()))
    heapq.heapify(queue)
    ans = 0
    while len(queue)>1:
        s = heapq.heappop(queue) + heapq.heappop(queue)
        ans+=s
        heapq.heappush(queue,s)

    print(ans)