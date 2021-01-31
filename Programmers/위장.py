def solution(clothes):
    answer = 1
    dic={}
    for i in range(len(clothes)):
        if clothes[i][1] in dic.keys():
            dic[clothes[i][1]]+=1
        else:
            dic[clothes[i][1]]=1
    for j in dic.values():
        answer*=j+1
    return answer-1
