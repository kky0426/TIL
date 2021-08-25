from sys import stdin
import bisect

M,N,L = map(int,stdin.readline().split())

spot = list(map(int,stdin.readline().split()))

animal = []
for _ in range(N):
    x,y = map(int,stdin.readline().split())
    animal.append((x,y))

spot.sort()
animal.sort()
ans = 0

for x,y in animal:
    idx = bisect.bisect_left(spot,x)
    if idx==0:
        if abs(spot[idx]-x)+y<=L:
            ans+=1
    elif idx == M:
        if abs(spot[idx-1]-x)+y<=L:
            ans+=1
    else:
        if abs(spot[idx]-x)+y<=L or abs(spot[idx-1]-x)+y<=L:
            ans+=1

print(ans)
