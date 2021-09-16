from sys import stdin
import heapq

N,K = map(int,stdin.readline().split())

visit= [False]*100001

visit[N] = True
queue=[]
heapq.heappush(queue,(0,N))
ans=-1
while queue:
    count,current = heapq.heappop(queue)
    if current == K:
        ans = count
        break

    if 0<=current*2<=100000 and not visit[current*2]:
        heapq.heappush(queue,(count,current*2))
        visit[current*2]

    if 0<=current+1<=100000 and not visit[current+1]:
        heapq.heappush(queue,(count+1,current+1))
        visit[current+1]

    if 0<=current-1<=100000 and not visit[current-1]:
        heapq.heappush(queue,(count+1,current-1))
        visit[current-1]
print(ans)
