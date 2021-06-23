def solution(record):
    answer = []
    dic = {}
    for i in range(len(record)):
        record[i] = list(record[i].split())
        
    for string in record:
        if string[0] == 'Enter' or string[0] == 'Change':
            dic[string[1]]=string[2]
    
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            answer.append(dic[record[i][1]]+"님이 들어왔습니다.")
        elif record[i][0] == 'Leave':
            answer.append(dic[record[i][1]]+"님이 나갔습니다.")
    return answer
