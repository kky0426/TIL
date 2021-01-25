def solution(answers):
    answer = []
    score = [0, 0, 0]
    for i in range(len(answers)):
        if (i % 5) +1 == answers[i]:
            score[0] += 1

    for j in range(len(answers)):
        if j % 2 == 0:
            if answers[j] == 2:
                score[1] += 1
        elif j % 8 == 1:
            if answers[j] == 1:
                score[1] += 1
        elif j % 8 == 3:
            if answers[j] == 3:
                score[1] += 1
        elif j%8 == 5:
            if answers[j]==4:
                score[1]+=1
        else:
            if answers[j] == 5:
                score[1] += 1

    for k in range(len(answers)):
        if k % 10 == 0 or k % 10 == 1:
            if answers[k] == 3:
                score[2] += 1
        elif k % 10 == 2 or k % 10 == 3:
            if answers[k] == 1:
                score[2] += 1
        elif k % 10 == 4 or k % 10 == 5:
            if answers[k] == 2:
                score[2] += 1
        elif k % 10 == 6 or k % 10 == 7:
            if answers[k] == 4:
                score[2] += 1
        else:
            if answers[k] == 5:
                score[2] += 1
    
    max_num = max(score)
    if max_num==score[0]:
        answer.append(1)
    if max_num==score[1]:
        answer.append(2)
    if max_num==score[2]:
        answer.append(3)
   
    return answer
