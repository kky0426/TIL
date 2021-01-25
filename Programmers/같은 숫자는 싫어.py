def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i<1:
            answer.append(arr[i])
        else:
            if arr[i]!=arr[i-1]:
                answer.append(arr[i])
        
    return answer
