from collections import deque


def solution(cacheSize, cities):
    answer = 0
    deq = deque()
    cities = [c.lower() for c in cities]
    if cacheSize < 1:
        answer = len(cities) * 5
    else:
        for city in cities:
            if city in deq:
                answer += 1
                deq.remove(city)
                deq.appendleft(city)
            else:
                if len(deq) < cacheSize:
                    deq.appendleft(city)
                    answer += 5
                else:
                    if deq:
                        deq.pop()
                    deq.appendleft(city)
                    answer += 5

    return answer
