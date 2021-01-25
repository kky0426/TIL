def solution(s):
    answer = ''
    ary=list(s)
    if len(s)%2==0:
        answer=ary[len(s)//2-1]+ary[len(s)//2]
    else:
        answer=ary[len(s)//2]
    return answer
