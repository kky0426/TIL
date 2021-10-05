from sys import stdin

wheels = [stdin.readline().rstrip() for _ in range(4)]

def rotate(wheel,d):
    if d == 1:
        wheel = wheel[-1]+wheel[:-1]
        return wheel
    else:
        wheel = wheel[1:] + wheel[0]
        return wheel

K = int(stdin.readline())
command = [list(map(int,stdin.readline().split())) for _ in range(K)]
for n,d in command:
    isRotate = [False]*4
    direction = [0]*4
    isRotate[n-1] = True
    direction[n-1] = d
    for i in range(n,4):
        if isRotate[i-1] and wheels[i][6]!=wheels[i-1][2]:
            isRotate[i]=True
            direction[i] = -direction[i-1]
        else:
            break
    for i in range(n-2,-1,-1):
        if isRotate[i+1] and wheels[i][2]!=wheels[i+1][6]:
            isRotate[i]=True
            direction[i] = -direction[i+1]
        else:
            break
    for i in range(4):
        if isRotate[i]:
            wheels[i] = rotate(wheels[i],direction[i])

ans = 0
for i in range(4):
    if wheels[i][0] == '1':
        ans+=2**i
print(ans)
