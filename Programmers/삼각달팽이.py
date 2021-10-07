def solution(n):
    answer = []
    ans = [[0 for _ in range(i)] for i in range(1,n+1)]
    
    x,y = -1,0
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x+=1
            elif i%3 == 1:
                y+=1
            elif i%3 == 2:
                x-=1
                y-=1
            ans[x][y] = num
            num+=1
    
    for arr in ans:
        answer.extend(arr)
    return answer
