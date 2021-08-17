from sys import stdin

N = int(stdin.readline())

liquid = list(map(int,stdin.readline().split()))

liquid.sort()

start = 0
end = len(liquid)-1

l1=0
l2=0
mem = float("inf")

while start<end:
    mix = liquid[start]+liquid[end]
    if abs(mix)<abs(mem):
        mem = mix
        l1 = start
        l2 = end

    if mix>0:
        end-=1
    else:
        start+=1

print(liquid[l1],liquid[l2])
