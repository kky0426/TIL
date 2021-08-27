from sys import stdin
import heapq

N = int(stdin.readline())

task = []
for _ in range(N):
    day,point = map(int,stdin.readline().split())
    task.append((point,day))

task.sort(key=lambda x:x[1])

heap = []
for point,day in task:
    if len(heap)<day:
        heapq.heappush(heap,(point,day))
    else:
        if heap[0][0]<point:
            heapq.heappop(heap)
            heapq.heappush(heap,(point,day))


ans = 0
for point,_ in heap:
    ans+=point

print(ans)
