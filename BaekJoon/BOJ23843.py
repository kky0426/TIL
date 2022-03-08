from sys import stdin
import heapq

N,M = map(int,stdin.readline().split())

times = list(map(int,stdin.readline().split()))
times.sort(reverse=True)
queue = []
cur = 0
for t in times:
    if len(queue)<M:
        heapq.heappush(queue,cur+t)
    else:
        cur = max(cur,heapq.heappop(queue))
        heapq.heappush(queue,cur+t)

print(max(queue))