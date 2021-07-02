def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000
    while left<=right:
        mid = left+(right-left)//2
        count = 0 
        for stone in stones:
            if stone-mid<=0:
                count+=1
            else:
                count=0
            if count>=k:
                break
        if count>=k:
            answer = mid
            right = mid-1
        else:
            left = mid+1
            
    return answer
