from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    x,y = map(int,stdin.readline().split())
    dis = y-x
    mid = int(dis**(1/2))
    ans = mid*2-1
    remain = dis-mid*mid
    if remain !=0:
        if remain<=mid:
            ans+=1
        else:
            ans+=2
    print(ans)
