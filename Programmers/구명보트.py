def solution(people, limit):
    answer = 0
    i=0
    j=len(people)-1
    people.sort(reverse=True)
    while (i<=j):
        if people[i]+people[j]<=limit:
            j-=1
        i+=1
        answer+=1


    return answer
