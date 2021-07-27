from sys import stdin

N=int(stdin.readline())

def solution(n):
    count=-1
    i=0
    while True:
        num=str(i)
        flag=True
        if len(num)<=1:
            pass
        else:
            for j in range(len(num)-1):
                if num[j]>num[j+1]:
                    continue
                else:
                    front=num[:j]
                    mid=str(int(num[j])+1)
                    end='0'+num[j+2:]
                    num= front+mid+end
                    flag=False
                    break

        if flag:
            count+=1
            if count==n:
                return i
            i += 1
        else:
            i=int(num)

if N>1022:
    print(-1)
else:
    print(solution(N))
