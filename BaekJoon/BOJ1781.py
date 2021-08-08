from sys import stdin
import heapq

N = int(stdin.readline())
queue=[]

for _ in range(N):
    d,v = map(int,stdin.readline().split())
    queue.append((d,v))

queue.sort(key= lambda x:(x[0]))
heap=[]
for d,v in queue:
    heapq.heappush(heap,v)
    if d<len(heap):
        heapq.heappop(heap)

print(sum(heap))
