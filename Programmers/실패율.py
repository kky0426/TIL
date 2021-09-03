def solution(N, stages):
    answer = []
    l=len(stages)
    dic = {n:0 for n in range(1,N+2)}
    for stage in stages:
        dic[stage]+=1
    ans = []
    print(dic)
    for i in range(1,N+1):
        total = 0
        for j in range(i,N+2):
            total+=dic[j]

        if total == 0:
            rate = 1
        else:
            rate = 1-dic[i]/total
        ans.append((rate,i))
    ans.sort()
    for v,i in ans:
        answer.append(i)
    return answer
