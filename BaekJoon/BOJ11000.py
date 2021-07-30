from sys import stdin
import heapq
from collections import deque

N=int(stdin.readline())

room=[]
subject=[]
for _ in range(N):
    s,e = map(int,stdin.readline().split())
    subject.append((s,e))

subject.sort(key=lambda x:x[0])
subject=deque(subject)

while subject:
    s,e=subject.popleft()
    if not room or room[0]>s:
        heapq.heappush(room,e)
    else:
        heapq.heappop(room)
        heapq.heappush(room,e)

print(len(room))
