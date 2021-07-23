from sys import stdin

N,M = map(int,stdin.readline().split())
desk=[]
for _ in range(N):
    desk.append(int(stdin.readline()))

start=0
end = M*max(desk)
ans=0
while start<=end:
    mid=start+(end-start)//2
    count=0
    for i in desk:
        count+=mid//i

    if count<M:
        start=mid+1
    else:
        ans=mid
        end=mid-1

print(ans)
