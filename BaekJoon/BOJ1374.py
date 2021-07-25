from sys import stdin
import heapq

N= int(stdin.readline())

heap=[]
queue=[]
for _ in range(N):
    n,s,e=map(int,stdin.readline().split())
    heapq.heappush(heap,(s,e,n))

s,e,n = heapq.heappop(heap);

heapq.heappush(queue,e)

while heap:
    s,e,n=heapq.heappop(heap)
    if queue[0]<=s:
        heapq.heappop(queue)
    heapq.heappush(queue,e)

print(len(queue))
