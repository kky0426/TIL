def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    set1=[]
    set2=[]
    for i in range(0,len(str1)-1):
        text=str1[i]+str1[i+1]
        if text.isalpha():
            set1.append(text)
    
    for i in range(0,len(str2)-1):
        text=str2[i]+str2[i+1]
        if text.isalpha():
            set2.append(text)
    if not set1 and not set2:
        return 65536
    
    inter=[]
    for i in set1:
        if i in set2:
            inter.append(i)
            set2.remove(i)
 
    if (len(set1)+len(set2)) == 0:
        return 65536
    elif len(inter) == 0:
        return 0
    else:
        return int((len(inter)/(len(set1)+len(set2))*65536))
