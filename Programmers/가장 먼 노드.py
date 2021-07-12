from collections import defaultdict
import heapq
INF = float('inf')

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    distance = [INF]*(n+1)
    distance[1]=0
    for u,v in edge:
        graph[u].append((1,v))
        graph[v].append((1,u))
    
    queue=[]
    heapq.heappush(queue,(0,1))
    while queue:
        wei,cur = heapq.heappop(queue)
        if distance[cur]<wei:
            continue
        
        for w,_next in graph[cur]:
            dis = wei+w
            if dis<distance[_next]:
                distance[_next]=dis
                heapq.heappush(queue,(dis,_next))
    
    for i in range(len(distance)):
        if distance[i]==INF:
            distance[i]=0
    m=max(distance)
    for dis in distance:
        if dis==m:
            answer+=1
    
    return answer
