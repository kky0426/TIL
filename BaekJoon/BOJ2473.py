from sys import stdin

N=int(stdin.readline())

liquid = list(map(int,stdin.readline().split()))
liquid.sort()

l,m,e = 0,0,0
mix=float('inf')
for i in range(len(liquid)-2):
    start=i+1
    end=len(liquid)-1
    while start<end:
        s=liquid[i]+liquid[start]+liquid[end]
        if abs(s)<abs(mix):
            l,m,e=i,start,end
            mix=s
        if s<0:
            start+=1
        elif s>0:
            end-=1
        else:
            break
print(liquid[l],liquid[m],liquid[e])
