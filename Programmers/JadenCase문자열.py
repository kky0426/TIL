def solution(s):
    answer = ''
    temp=list(s.split(" "))
    for i in range(len(temp)):
        temp[i]=temp[i].capitalize()
    answer=" ".join(temp)
    return answer
