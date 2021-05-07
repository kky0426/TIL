from sys import stdin

N,M=map(int,stdin.readline().rstrip().split())

nums=list(map(int,stdin.readline().rstrip().split()))

start,end=0,0

sum=0
ans=0
while True:
    if end==N:
        if start==end:
            break
        else:
            sum-=nums[start]
            start+=1
    elif sum<M:
        sum+=nums[end]
        end+=1
    else:
        sum-=nums[start]
        start+=1
        
    if sum==M:
        ans+=1

print(ans)
