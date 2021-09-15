from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    start,target = map(int,stdin.readline().split())
    visit = [False]*10000
    queue = deque()
    queue.append((start,""))
    ans = ""
    visit[start]=True
    while True:
        num,command = queue.popleft()
        if num == target:
            ans = command
            break

        D = (num*2)%10000
        if not visit[D]:
            queue.append((D,command+"D"))
            visit[D] = True

        S = num-1 if num!=0 else 9999
        if not visit[S]:
            queue.append((S,command+"S"))
            visit[S] = True


        L = int(num%1000 * 10 + num//1000)
        if  not visit[L]:
            queue.append((L,command+"L"))
            visit[L] = True

        R = int(num%10*1000 + num//10)
        if  not visit[R]:
            queue.append((R,command+"R"))
            visit[R] = True

    print(ans)
