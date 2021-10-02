from sys import stdin

N,L = map(int,stdin.readline().split())

puddle = [list(map(int,stdin.readline().split())) for _ in range(N)]
puddle.sort()

idx = 0
ans = 0
for l,r in puddle:
    if r<idx:
        continue
    idx = max(idx,l)
    count = (r-idx)//L
    if (r-idx)%L !=0: count+=1
    ans+=count
    idx+=count*L

print(ans)
