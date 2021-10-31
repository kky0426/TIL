from sys import stdin

N = int(stdin.readline())

queue = []
ans = ""
for _ in range(N):
    command = list(stdin.readline().split())
    if command[0] == 'type':
        ans+=command[1]
        queue.append((ans,int(command[2])))
    else:
        t1,t2 = command[1],command[2]
        time = int(t2)-int(t1)
        idx = len(queue)-1
        while idx>=0:
            if queue[idx][1]<time:
                ans = queue[idx][0]
                break
            else:
                ans = ""
            idx-=1
        queue.append((ans,int(t2)))
print(ans)
