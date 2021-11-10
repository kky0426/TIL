def solution(gems):
    answer = []
    k = len(set(gems))
    N = len(gems)
    
    left = 0
    right = 0
    dic = {}
    while True:
        if right == N and left == N:
            break
        elif right == N:
            if len(dic)>=k:
                answer.append([left,right])
            
            if gems[left] in dic:
                if dic[gems[left]]>1:
                    dic[gems[left]]-=1
                else:
                    del dic[gems[left]]
            left+=1
    
        else:   
            if len(dic)>=k:
                answer.append([left,right])
                dic[gems[left]]-=1
                if dic[gems[left]] == 0:
                    del dic[gems[left]]
                left+=1
            else:
                if gems[right] in dic:
                    dic[gems[right]]+=1
                else:
                    dic[gems[right]]=1
                right+=1
    
    answer.sort(key=lambda x:(x[1]-x[0],x[0])) 
    return [answer[0][0]+1,answer[0][1]]
