def solution(s):
    answer = ''
    num=list(map(int,s.split()))
    answer=str(min(num))+" "+str(max(num))
    return answer
