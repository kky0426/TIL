from sys import stdin

N = int(stdin.readline())

point = [list(map(int,stdin.readline().split())) for _ in range(N)]

def calc(src,des):
    return abs(src[0]-des[0])+abs(src[1]-des[1])

total = 0
for i in range(N-1):
    total+=calc(point[i],point[i+1])

skip = 0
for i in range(1,N-1):
    pre = point[i-1]
    cur = point[i]
    next = point[i+1]
    dis = calc(pre,cur)+calc(cur,next)
    st = calc(pre,next)
    skip = max(skip,dis-st)

print(total-skip)
