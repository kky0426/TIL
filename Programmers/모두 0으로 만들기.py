from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):
    answer = 0
    if sum(a)!=0:
        return -1
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visit = [False]*len(a)
    def dfs(x):
        visit[x]=True
        for y in graph[x]:
            if not visit[y]:
                a[x]+=dfs(y)
        nonlocal answer
        answer+=abs(a[x])
        return a[x]
    dfs(0)
    return answer
