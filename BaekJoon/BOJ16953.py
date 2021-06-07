from sys import stdin
N,M = map(int,stdin.readline().split())

ans=0

while True:
    if N==M:
        print(ans+1)
        break
    elif N > M:
        print(-1)
        break;
        
    if M%10==1:
        M=M//10
    elif M%2==0:
        M=M//2
    else:
        print(-1)
        break
    ans+=1
