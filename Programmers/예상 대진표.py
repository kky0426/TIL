def solution(n,a,b):
    answer=1
    while True:
        if (a%2==0 and a-b==1) or (a%2!=0 and b-a==1):
            return answer
        
        if a%2==0:
            a=a//2
        else:
            a=a//2 +1
        
        if b%2==0:
            b=b//2
        else:
            b=b//2 +1
        answer+=1
        n=n//2
