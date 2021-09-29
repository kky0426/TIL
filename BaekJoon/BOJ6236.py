from sys import stdin

N,M = map(int,stdin.readline().split())

spend = [int(stdin.readline()) for _ in range(N)]

left = 0
right = 10000*100000
max_m = max(spend)

while left<=right:
    mid = left+(right-left)//2
    count = 1
    money = mid
    for m in spend:
        money-=m
        if money<0:
            count+=1
            money = mid-m

    if count>M or mid<max_m:
        left = mid+1
    else:
        right = mid-1
        ans = mid
print(ans)
