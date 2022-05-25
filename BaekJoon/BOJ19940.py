from sys import stdin
from collections import deque

def bfs(target):
    queue = deque()
    visit = [False]*61
    queue.append((0,0,0,0,0,0))
    visit[0] = True
    while queue:
        count,time,ADDT,MINT,ADDO,MINO = queue.popleft()
        if time == target:
            return count,[ADDT,MINT,ADDO,MINO]

        if 0<=time-1<=60 and not visit[time-1]:
            visit[time-1] = True
            queue.append((count+1,time-1,ADDT,MINT,ADDO,MINO+1))
        if 0<=time+1<=60 and not visit[time+1]:
            visit[time+1] = True
            queue.append((count+1,time+1,ADDT,MINT,ADDO+1,MINO))
        if 0<=time-10<=60 and not visit[time-10]:
            visit[time-10] = True
            queue.append((count+1,time-10,ADDT,MINT+1,ADDO,MINO))
        if 0<=time+10<=60 and not visit[time+10]:
            visit[time+10] = True
            queue.append((count+1,time+10,ADDT+1,MINT,ADDO,MINO))

T = int(stdin.readline())

for _ in range(T):
    time = int(stdin.readline())
    k = time//60
    mod = time%60
    count1,res1 = bfs(mod)
    count2,res2 = bfs(60-mod)
    res2[0], res2[1], res2[2], res2[3] = res2[1], res2[0], res2[3], res2[2]
    if k+count1 < k+1+count2:
        ans = [k]+res1
    elif k+count1>k+1+count2:
        ans = [k+1]+res2
    else:
        temp = []
        temp.append([k]+res1)
        temp.append([k+1]+res2)
        temp.sort(key=lambda x:"".join(map(str,x)))
        ans = temp[0]
    print(*ans)



