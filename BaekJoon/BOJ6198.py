from sys import stdin

N = int(stdin.readline())

building = [int(stdin.readline()) for _ in range(N)]
stack = []
ans = 0
for i in range(N):
    while stack and stack[-1]<=building[i]:
        stack.pop()
    stack.append(building[i])
    ans+=len(stack)-1

print(ans)
