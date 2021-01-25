def solution(priorities, location):
    answer = 0
    n=len(priorities)
    mem=[]
    p_idx=[]
    for i in range(len(priorities)):
        p_idx.append((i,priorities[i]))
        
    while(p_idx):
        p_num=p_idx.pop(0)
        if p_num[1]!=max(priorities):
            p_idx.append(p_num)
        else:
            mem.append(p_num)
            priorities.pop(priorities.index(max(priorities)))
   
    for i in range(len(mem)):
        if mem[i][0] == location:
            answer=i+1
    return answer
