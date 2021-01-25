def solution(n, lost, reserve):
    
    temp=list(set(lost)-set(reserve))
    reserve=list(set(reserve)-set(lost))
    lost=temp

    answer=n-len(lost)
    for i in lost:
        if i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
        elif i-1 in reserve:
            answer+=1
    return answer
