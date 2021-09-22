from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    nums = list(map(int,stdin.readline().split()))

    nums.sort()
    ans = deque()
    flag = True
    while nums:
        if flag:
            ans.append(nums.pop())
        else:
            ans.appendleft(nums.pop())
        flag = not flag
    answer = abs(ans[0]-ans[-1])
    for i in range(N-1):
        answer = max(answer,abs(ans[i]-ans[i+1]))
    print(answer)
