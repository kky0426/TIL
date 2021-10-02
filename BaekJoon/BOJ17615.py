from sys import stdin

N = int(stdin.readline())
ball = stdin.readline().rstrip()

ans = float("inf")

flag = False
count=0
for i in range(N):
    if ball[i] == 'R':
        if flag:count+=1
    else:
        flag=True
ans = min(ans,count)

flag = False
count = 0
for i in range(N):
    if ball[i] == 'B':
        if flag: count += 1
    else:
        flag = True
ans = min(ans,count)

flag = False
count = 0
for i in range(N-1,-1,-1):
    if ball[i] == 'R':
        if flag : count += 1
    else:
        flag = True
ans = min(ans,count)

flag = False
count = 0
for i in range(N-1,-1,-1):
    if ball[i] == 'B':
        if flag: count += 1
    else:
        flag = True
ans = min(ans,count)

print(ans)
