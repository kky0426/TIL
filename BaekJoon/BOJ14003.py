from sys import stdin
import bisect

N = int(stdin.readline())

nums = list(map(int,stdin.readline().split()))

lis = []
trace = []
length = 0
for i in range(N):
    idx = bisect.bisect_left(lis,nums[i])
    if idx == len(lis):
        lis.append(nums[i])
        length+=1
    else:
        lis[idx] = nums[i]
    trace.append(idx)

print(len(lis))

ans = []
for i in range(len(trace)-1,-1,-1):
    if trace[i] == length-1:
        ans.append(nums[i])
        length-=1

print(*reversed(ans))
