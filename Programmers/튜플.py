from collections import Counter

def solution(s):
    answer = []
    s=list(s.replace("{","").replace("}","").split(","))
    tuples = Counter(s).most_common()
    for k,v in tuples:
        answer.append(int(k))
    return answer
