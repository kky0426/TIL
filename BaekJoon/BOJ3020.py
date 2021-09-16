from sys import stdin
import bisect

N,H = map(int,stdin.readline().split())

jong = []
suk = []

for i in range(N):
    num = int(stdin.readline())
    if i%2==0:
        suk.append(num)
    else:
        jong.append(num)
jong.sort()
suk.sort()

ans = float("inf")
count= 0
for i in range(1,H+1):
    bottom = N//2 - bisect.bisect_left(suk,i+1)
    top = N//2 - bisect.bisect_left(jong,H-i)
    if ans>bottom+top:
        ans = bottom+top
        count = 1
    elif ans == bottom+top:
        count+=1

print(ans,count)
