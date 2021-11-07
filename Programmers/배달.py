from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    distance = [float("inf")]*(N+1)
    heap = []
    graph = defaultdict(list)
    
    for u,v,w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    distance[1] = 0
    heapq.heappush(heap,(0,1))
    while heap:
        dis,node = heapq.heappop(heap)
        
        if dis>distance[node]:
            continue
        
        for next_node,w in graph[node]:
            if distance[next_node]>dis+w:
                distance[next_node] = dis+w
                heapq.heappush(heap,(distance[next_node],next_node))
    
    
    for i in range(1,N+1):
        if distance[i]<=K:
            answer+=1

    return answer
