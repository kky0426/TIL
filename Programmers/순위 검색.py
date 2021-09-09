from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    total = []
    for line in info:
        temp = line.split()
        category = temp[:-1]
        score = int(temp[-1])
        total.append(score)
        for i in range(1,5):
            combi = list(combinations(category,i))
            for cate in combi:
                dic["-".join(cate)].append(score)
    total.sort()
    for k,v in dic.items():
        v.sort()
        
    for q in query:
        temp = q.replace("and","").replace("-","").split()
        score = int(temp[-1])
        condition = "-".join(temp[:-1])
        if not condition:
            search = total
        else:
            search = dic[condition]
        idx = bisect.bisect_left(search,score)
        answer.append(len(search)-idx)
    return answer
