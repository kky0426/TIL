from itertools import combinations


def menu_n(orders, n):
    menu = []
    dic = {}
    for i in range(len(orders)):
        temp = []
        comb = list(combinations(orders[i], n))
        for j in range(len(comb)):
            comb_s = list(comb[j])
            comb_s.sort()
            temp.append("".join(comb_s))
        temp_=set(temp)
        menu.extend(temp_)

    for i in menu:
        try:
            dic[i] += 1
        except:
            dic[i] = 1

    new = []
    for key, value in dic.items():
        if max(dic.values()) == value and value > 1:
            new.append(key)
    return new


def solution(orders, course):
    answer = []
    temp = []
    for i in course:
        answer.extend(menu_n(orders, i))


    answer.sort()
    return answer
