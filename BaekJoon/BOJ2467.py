from sys import stdin

N=int(stdin.readline())

liquid = list(map(int,stdin.readline().split()))

start=0
end=len(liquid)-1

mem=float("inf")
l=0
r=0
while start<end:
    mix=liquid[start]+liquid[end]
    if abs(mix)<abs(mem):
        l=start
        r=end
        mem=mix
    if mix<0:
        start+=1
    else:
        end-=1

print(liquid[l],liquid[r])
