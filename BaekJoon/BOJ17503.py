from sys import stdin

N,M,K = map(int,stdin.readline().split())

beer = [list(map(int,stdin.readline().split())) for _ in range(K)]

beer.sort(key=lambda x:(-x[0]))


ans = 0
left = 0
right = 2**31

while left<=right:
    mid = (left+right)//2
    s = 0
    count = 0
    for v,c in beer:
        if count == N:
            break
        if c<=mid:
            s+=v
            count+=1

    if count<N:
        left = mid+1
        continue

    if s>=M:
        ans = mid
        right = mid-1
    else:
        left = mid+1

print(ans if ans!=0 else -1)
