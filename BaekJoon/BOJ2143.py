from sys import stdin
import bisect

T=int(stdin.readline())

N=int(stdin.readline())
A=list(map(int,stdin.readline().split()))

M=int(stdin.readline())
B=list(map(int,stdin.readline().split()))

sumA,sumB={},{}

for i in range(N):
    s=0
    for j in range(i,N):
        s+=A[j]
        if s in sumA:
            sumA[s]+=1
        else:
            sumA[s]=1
ans=0
for i in range(M):
    s=0
    for j in range(i,M):
        s+=B[j]
        if s in sumB:
            sumB[s]+=1
        else:
            sumB[s]=1

for k,v in sumA.items():
    if T-k in sumB:
        ans+=v*sumB[T-k]

print(ans)
