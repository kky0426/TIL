def solution(n, costs):
    
    def find(x):
        if x == parent[x]:
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
    
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])
    count = 0
    for u,v,w in costs:
        if count == n-1:
            break
        if find(u)!=find(v):
            union(u,v)
            answer+=w
            count+=1
    return answer
