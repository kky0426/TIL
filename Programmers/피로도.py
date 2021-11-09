def permutation(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],n-1):
                yield [arr[i]]+next
            
def solution(k, dungeons):
    answer = 0
    N = len(dungeons)
    
    for candidate in permutation(dungeons,N):
        current = k
        count = 0
        for need,consume in candidate:
            if current>=need:
                current-=consume
                count+=1
        answer = max(answer,count)
    return answer
