def combinations(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for nex in combinations(arr[i:],n-1):
                yield [arr[i]]+nex
                
def solution(n, info):
    idx = [i for i in range(11)]
    ans = []
    answer = []
    for candidate in combinations(idx,n):
        rion = 0
        apeach = 0
        arr = [0]*11
        max_diff = 0
        for i in candidate:
            arr[i]+=1
        
        for i in range(11):
            if arr[i]>info[i]:
                rion+=10-i
            elif info[i]>0:
                apeach+=10-i
        
        diff = rion-apeach
        if diff>=max_diff:
            max_diff = diff
            ans.append((diff,arr))
    if not ans:
        return [-1]
    
    ans.sort(reverse=True)
    max_diff = ans[0][0]
    if max_diff == 0:
        return [-1]
    for diff,arr in ans:
        if diff == max_diff:
            answer.append(arr[::-1])
        else:
            break
    answer.sort(reverse=True)
    return answer[0][::-1]
