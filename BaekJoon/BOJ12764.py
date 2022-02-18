from sys import stdin
import heapq

N = int(stdin.readline())

time = [list(map(int,stdin.readline().split())) for _ in range(N)]
time.sort(key = lambda x:x[0])

visit = [0]*N
empty = [i for i in range(N)]
heapq.heapify(empty)
queue = []
seat = 0
for s,e in time:
    while queue:
        if queue[0][0]<=s:
            n = queue[0][1]
            heapq.heappush(empty,n)
            heapq.heappop(queue)
        else:
            break

    idx = heapq.heappop(empty)
    visit[idx]+=1
    heapq.heappush(queue,(e,idx))

ans = []
for n in visit:
    if n == 0:
        break
    ans.append(n)
print(len(ans))
print(*ans)

