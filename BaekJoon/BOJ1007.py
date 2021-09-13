from sys import stdin
from itertools import combinations


'''
def combination(arr,n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i:],n-1):
                yield [arr[i]]+next
'''
T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    spot = []

    for _ in range(N):
        x,y = map(int,stdin.readline().split())
        spot.append((x,y))
    ans = float("inf")
    U = set(spot)
    for candidate in combinations(spot,N//2):
        s2 = list(U-set(candidate))
        x1,y1=0,0
        for x,y in candidate:
            x1+=x
            y1+=y
        x2,y2 = 0,0
        for x,y in s2:
            x2+=x
            y2+=y

        length =((x1-x2)**2+(y1-y2)**2)**(1/2)
        ans = min(ans,length)

    print(ans)
