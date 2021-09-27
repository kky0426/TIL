from sys import stdin

N,K,B = map(int,stdin.readline().split())

light = [0]*N
for _ in range(B):
    n = int(stdin.readline())
    light[n-1] = 1

for i in range(N-1):
    light[i+1]+=light[i]

left=0
ans = N
while left+K<N:
    ans = min(ans,light[left+K]-light[left])
    left+=1

print(ans)
