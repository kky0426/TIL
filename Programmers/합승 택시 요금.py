def solution(n, s, a, b, fares):
    answer = float("inf")
    graph = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
    for u,v,w in fares:
        graph[u][v] = w
        graph[v][u] = w
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    graph[i][j] = 0
                if graph[i][j]> graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]
    
    for i in range(1,n+1):
        answer = min(answer,graph[s][i]+graph[i][a]+graph[i][b])
    
    return answer
