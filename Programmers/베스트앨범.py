def solution(genres, plays):
    answer = []
    
    genres_dic={}
    for i in range(len(genres)):
        try:
            genres_dic[genres[i]]+=plays[i]
        except:
            genres_dic[genres[i]]=plays[i]
    genres_dic=dict(sorted(genres_dic.items(),key=lambda x:x[1],reverse=True)) 
    
    for genre in genres_dic.keys():
        temp=[]
        for j in range(len(genres)):
            if genres[j] == genre:
                temp.append([j,plays[j]])
        temp=sorted(temp,key=lambda x:x[1],reverse=True)
        if len(temp)>1:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])
            
            
    return answer
