
def solution(n, computers):
    answer = set()
    parent = [i for i in range(n)]
    
    def find(x):
        if x==parent[x]:
            return x
        else:
            return find(parent[x])
    
    def union(x,y):
        x = find(x)
        y = find(y)
        if x<y:
            parent[y] = x
        else:
            parent[x] = y
            
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i,j)
    
    for i in range(n):
        answer.add(find(i))
    
    return len(answer)
