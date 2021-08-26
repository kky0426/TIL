from sys import stdin
import heapq

N = int(stdin.readline())

lecture = []
for _ in range(N):
    pay,time = map(int,stdin.readline().split())
    lecture.append((pay,time))

lecture.sort(key=lambda x:x[1])

heap = []

for pay,time in lecture:
    if len(heap)<time:
        heapq.heappush(heap,(pay,time))
    else:
        if heap[0][0]<pay:
            heapq.heappop(heap)
            heapq.heappush(heap,(pay,time))
ans = 0
for p,t in heap:
    ans+=p
print(ans)
