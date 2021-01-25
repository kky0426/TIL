def solution(n):
    answer = 0
    ary=[]
    while(n>0):
        ary.append(n%3)
        n=n//3
    ary.reverse()
    for i in range(len(ary)):
        answer += 3**i * ary[i]
    return answer
