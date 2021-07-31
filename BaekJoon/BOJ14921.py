from sys import stdin

N = int(stdin.readline())

liquid = list(map(int,stdin.readline().split()))

start=0
end = N-1
ans= 200000000
l,r=0,0

while start<end:
    mix = liquid[start]+liquid[end]
    if abs(mix)<abs(ans):
        ans=mix

    if mix>0:
        end-=1
    else:
        start+=1

print(ans)
