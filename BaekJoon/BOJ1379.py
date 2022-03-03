from sys import stdin
import heapq

N = int(stdin.readline())

lecture = [list(map(int,stdin.readline().split())) for _ in range(N)]

lecture.sort(key=lambda x:(x[1],x[2]))

heap = []
room = [i for i in range(1,N+1)]
heapq.heapify(room)

ans = [0]*(N+1)

for n,s,e in lecture:
    while heap and heap[0][0]<=s:
        _,r = heapq.heappop(heap)
        heapq.heappush(room,r)

    room_num = heapq.heappop(room)
    heapq.heappush(heap,(e,room_num))
    ans[n] = room_num
print(max(ans))
for n in ans[1:]:
    print(n)
