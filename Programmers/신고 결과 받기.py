from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    dic = defaultdict(list)
    
    reported = {}
    for i in id_list:
        reported[i] = 0
        
    for rep in report:
        u,r = rep.split()
        if r not in dic[u]:
            dic[u].append(r)
            reported[r]+=1
    
    for user in id_list:
        count=0
        for report_user in dic[user]:
            if reported[report_user]>=k:
                count+=1
        answer.append(count)
    return answer
