def solution(s):
    answer = []
    
    for i in range(1,len(s)//2+2):
        result=''
        slice_n=s[:i]
        count = 1
        for j in range(i,len(s)+i,i):
            if s[j:j+i] == slice_n:
                count +=1
            else:
                if count == 1:
                    result+=slice_n
                else:
                    result=result+str(count)+slice_n
                
                slice_n=s[j:j+i]
                count = 1
                
        answer.append(len(result))
     
    return  min(answer)