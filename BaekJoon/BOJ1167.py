#다익스트라 풀이
from sys import stdin
from collections import defaultdict
import heapq

V = int(stdin.readline())

graph = defaultdict(list)

for _ in range(V):
    line = list(map(int,stdin.readline().split()))
    u = line[0]
    for i in range(1,len(line)-1,2):
        graph[u].append((line[i],line[i+1]))
        graph[line[i]].append((u,line[i+1]))

def dijkstra(start):
    distance = [float("inf")]*(V+1)
    distance[start] = 0

    queue = []
    queue.append((0,start))
    while queue:
        dis,cur = heapq.heappop(queue)
        if dis>distance[cur]:
            continue

        for n,w in graph[cur]:
            if dis+w<distance[n]:
                distance[n] = dis+w
                heapq.heappush(queue,(distance[n],n))

    max_dis = 0
    idx = 0
    for i in range(1,len(distance)):
        if distance[i] != float("inf") and max_dis<distance[i]:
            max_dis = distance[i]
            idx = i
    return max_dis,idx

far,idx = dijkstra(1)
ans,temp_idx = dijkstra(idx)
print(ans)



"""
dfs 풀이

from sys import stdin
from collections import defaultdict


V = int(stdin.readline())

graph = defaultdict(list)

for _ in range(V):
    line = list(map(int,stdin.readline().split()))
    u = line[0]
    for i in range(1,len(line)-1,2):
        graph[u].append((line[i],line[i+1]))


visit = [False]*(V+1)

ans = 0

def dfs(node,parent):
    if visit[node]:
        return 0

    visit[node] = True
    dis = 0
    for n,w in graph[node]:
        if n == parent:
            continue
        cur = dfs(n,node)+w+dis
        global ans
        ans = max(ans,cur)
        dis = max(dis,cur-dis)
    return dis

dfs(1,-1)
print(ans)
"""
