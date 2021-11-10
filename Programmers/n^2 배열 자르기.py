def solution(n, left, right):
    answer = []
    for idx in range(left,right+1):
        i = idx//n
        j = idx%n
        answer.append(max(i,j)+1)
    return answer
