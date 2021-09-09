from itertools import combinations

def solution(relation):
    answer = 0
    N = len(relation[0])
    M = len(relation)
    candidate = []
    for i in range(1,N+1):
        candidate.extend(list(combinations(range(N),i)))
    
    
    ans = []
    for keys in candidate:
        temp = []
        for rows in relation:
            temp_ = tuple(rows[key] for key in keys)
            temp.append(temp_)
        

        if len(set(temp)) == M:
            ans.append(keys)
    
    ans_set = set(ans)
    key_len = len(ans)
    for i in range(key_len-1):
        for j in range(i+1,key_len):
            if set(ans[i]) == set(ans[i])&set(ans[j]):
                ans_set.discard(ans[j])
          
    return len(ans_set)
