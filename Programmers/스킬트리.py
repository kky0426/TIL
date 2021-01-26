def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        temp=[]
        flag=True
        
        for i in skills:
            if i in skill:
                temp.append(i)
        
        for j in range(len(temp)):
            if temp[j]!=skill[j]:
                flag=False
        
        if flag==True:
            answer+=1
        
    return answer
