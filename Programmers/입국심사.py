def solution(n, times):
    answer = 0
    left = 1
    right = (len(times)+1)*max(times)
    
    while left<=right:
        mid = (left+right)//2
        count = 0
        for i in range(len(times)):
            count+=mid//times[i]
     
        if count<n:
            left = mid+1
        else:
            answer = mid
            right = mid-1
    return answer
