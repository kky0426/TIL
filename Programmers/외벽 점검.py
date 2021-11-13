def permutation(arr,n):
    for i in range(len(arr)):
        if n==1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],n-1):\
                yield [arr[i]]+next
                
def solution(n, weak, dist):
    answer = float("inf")
    k = len(weak)
    temp = [n+weak[i] for i in range(k)]
    weak.extend(temp)
    print(weak)
    for start in range(k):
        for candidate in permutation(dist,len(dist)):
            count = 1
            idx = 0
            possible = weak[start]+candidate[idx]
            for spot in weak[start:start+k]:
                if spot>possible:
                    count+=1                   
                    if count>len(dist):break                     
                    idx+=1
                    possible = spot+candidate[idx]
                
            answer = min(answer,count)
    
    if answer>len(dist):
        return -1
            
    return answer
