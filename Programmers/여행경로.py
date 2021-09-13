from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(graph)
    for src,des in tickets:
        graph[src].append(des)
    
    for k,v in graph.items():
        v.sort(reverse = True)
    
    
    def dfs():
        stack = ["ICN"]
        path = []
        
        while stack:
            current = stack[-1]
            if current not in graph or len(graph[current]) == 0:
                path.append(stack.pop())
            else:
                stack.append(graph[current].pop())
        path.reverse()
        return path
    answer = dfs()
    
    return answer
