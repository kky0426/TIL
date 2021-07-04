def solution(n):
    answer = []
    def hanoi(n,start,target,temp):
        if n==1:
            answer.append([start,target])
            return
        hanoi(n-1,start,temp,target)
        answer.append([start,target])
        hanoi(n-1,temp,target,start)
        
    hanoi(n,1,3,2)

    return answer
