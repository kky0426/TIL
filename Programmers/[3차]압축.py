def solution(msg):
    answer = []
    dic = {chr(ord("A") + i): i + 1 for i in range(26)}

    N = len(msg)
    w = ""
    for i in range(N):
        w += msg[i]
        if i + 1 < N:
            c = msg[i + 1]
            wc = w + c
            if wc in dic:
                continue
            w = wc
        dic[w] = dic[w] + 1
        answer.append(dic[w])
        w = ""
    return answer
