def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        try:
            dic[i]+=1
        except:
            dic[i]=1
            
    for k in completion:
        dic[k]-=1
        
    for key,value in dic.items():
        if value ==1:
            answer = key
            break
        
    return answer
