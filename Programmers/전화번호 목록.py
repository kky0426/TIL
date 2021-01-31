def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i==j:
                continue
            else:
                if phone_book[j].startswith(phone_book[i]):
                    return False
    return answer
