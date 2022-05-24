from sys import stdin
import heapq

N = int(stdin.readline())
time = [list(map(int,stdin.readline().split())) for _ in range(N)]

time.sort(key=lambda x:x[0])
ans = 0
queue = []
for s,e in time:
    while queue and queue[0]<=s:
        heapq.heappop(queue)
    heapq.heappush(queue,e)
    ans = max(ans,len(queue))

print(ans)