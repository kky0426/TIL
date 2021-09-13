def solution(weights, head2head):
    answer = []
    N = len(weights)
    people = []
    for i in range(N):
        count = 0
        win = 0
        lose = 0
        for j in range(N):
            if head2head[i][j] == 'W':
                win+=1
                if weights[i]<weights[j]:
                    count+=1
            elif head2head[i][j] == 'L':
                lose+=1
        if lose+win == 0:
            rate = 0
        else:
            rate = win/(win+lose)
        
        people.append((rate,count,weights[i],i))
    people.sort(key = lambda x:(-x[0],-x[1],-x[2],x[3]))

    for i in range(N):
        answer.append(people[i][3]+1)
    return answer
