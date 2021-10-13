from sys import stdin

N,p1,p2 = map(int,stdin.readline().split())
if p1>p2:
    p1,p2 = p2,p1
ans = 1
while True:
    if p1%2 == 1 and p1+1 == p2:
        print(ans)
        break

    if p1%2 == 0:
        p1 = p1//2
    else:
        p1 = p1//2 + 1

    if p2%2 == 0:
        p2 = p2//2
    else:
        p2 = p2//2 + 1
    ans+=1
