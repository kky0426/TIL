def solution(n, results):
    answer = 0
    rank = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for a,b in results:
        rank[a][b] = 1
        rank[b][a] = -1
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if rank[i][k] == 1 and rank[k][j] == 1:
                    rank[i][j] = 1
                elif rank[i][k] == -1 and rank[k][j] == -1:
                    rank[i][j] = -1
                    
    for i in range(1,n+1):
        if rank[i].count(0) == 2:
            answer+=1
    return answer
