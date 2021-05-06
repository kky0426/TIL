from sys import stdin

N=int(stdin.readline().rstrip())
nums=list(map(int,stdin.readline().rstrip().split()))

ans=[-1]*N

stack=[]
stack.append(0)
for i in range(N):
    while stack and nums[i]>nums[stack[-1]]:
        last=stack.pop()
        ans[last]=nums[i]
    stack.append(i)

print(" ".join(map(str,ans)))
