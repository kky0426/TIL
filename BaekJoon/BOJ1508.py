from sys import stdin

N,M,K = map(int,stdin.readline().split())

place = list(map(int,stdin.readline().split()))

left = 0
right = place[-1]
dis = 0
while left<=right:
    mid = (left+right)//2
    count = 0
    pre = -1
    for p in place:
        if pre<=p:
            pre = p+mid
            count+=1

    if count>=M:
        dis = mid
        left = mid+1
    else:
        right = mid-1


ans = ""
pre = -1
count = 0
for p in place:
    if pre<=p and count<M:
        ans+="1"
        count+=1
        pre = p+dis
    else:
        ans+="0"

print(ans)