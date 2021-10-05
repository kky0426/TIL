from sys import stdin

N = int(stdin.readline())

nums = [int(stdin.readline()) for _ in range(N)]
stack = []
ans = []

idx = 0
for i in range(1,N+1):
    stack.append(i)
    ans.append('+')
    while stack and stack[-1] == nums[idx]:
        stack.pop()
        ans.append('-')
        idx+=1

if stack:
    print("NO")
else:
    for op in ans:
        print(op)
