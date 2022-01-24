import math
from collections import defaultdict

def convert_time(time):
    h,m = time.split(":")
    h = int(h)
    m = int(m)
    return 60*h+m

def solution(fees, records):
    answer = []
    basic_time,basic_fee,unit_time,unit_fee = fees
    dic = defaultdict(list)
    for record in records:
        time,car,content = record.split()
        time = convert_time(time)
        if content == 'IN':
            dic[car].append([time,None])
        else:
            dic[car][-1][1] = time
    ans = []
    for car,history in dic.items():
        if history[-1][1] == None:
            history[-1][1] = convert_time("23:59")
        total = 0
        price = 0
        for i,o in history:
            total+=o-i
        if total<=basic_time:
            price = basic_fee
        else:
            over_time = total-basic_time
            price = basic_fee + math.ceil(over_time/unit_time)*unit_fee
        ans.append([car,price])
    ans.sort()
    for c,p in ans:
        answer.append(p)
    return answer
