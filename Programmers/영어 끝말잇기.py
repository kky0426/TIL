def solution(n, words):
    answer = []

    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1]:
            answer.append([i%n+1,i//n+1])
            return answer[0]
        else:
            if words[i] in words[:i]:
                answer.append([i%n+1,i//n+1])
                return answer[0]
    return [0,0]
