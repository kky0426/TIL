from sys import stdin
import heapq
from collections import defaultdict

N,M,S,E = map(int,stdin.readline().split())
graph = defaultdict(list)
S*=2
E*=2
for _ in range(M):
    u,v,L,t1,t2 = map(int,stdin.readline().split())
    graph[u].append((v,L*2,t1))
    graph[v].append((u,L*2,t2))

def dijkstra():
    distance = [float("inf")]*(N+1)
    distance[1] = 0
    queue = []
    heapq.heappush(queue,(0,1))

    while queue:
        dis,node = heapq.heappop(queue)
        if dis>distance[node]:
            continue

        for n,w,t in graph[node]:
            if t == 0:
                if dis+w<distance[n]:
                    distance[n] = dis+w
                    heapq.heappush(queue,(distance[n],n))
            else:
                if dis<S:
                    if dis+w<=S:
                        new_dis = dis+w
                    else:
                        pre = S-dis
                        remain = w-pre
                        duration = E-S
                        if remain*2<=duration:
                            new_dis = dis+pre+remain*2
                        else:
                            new_dis = dis+w+duration//2
                elif S<=dis<E:
                    duration = E-dis
                    if duration>=w*2:
                        new_dis = dis+w*2
                    else:
                        new_dis = dis+w+duration//2
                else:
                    new_dis = dis+w

                if new_dis<distance[n]:
                    distance[n] = new_dis
                    heapq.heappush(queue,(distance[n],n))
    return max(distance[1:])

ans = dijkstra()
if ans%2 == 0:
    print(ans//2)
else:
    print(ans//2+0.5)