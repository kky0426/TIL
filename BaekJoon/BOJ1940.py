from sys import stdin

N=int(stdin.readline())
M=int(stdin.readline())

mater=list(map(int,stdin.readline().split()))
mater.sort()

start=0
end = len(mater)-1
ans=0

while start<end:
    s=mater[start]+mater[end]
    if s==M:
        ans+=1
        start+=1
        end-=1
    elif s<M:
        start+=1
    else:
        end-=1

print(ans)
