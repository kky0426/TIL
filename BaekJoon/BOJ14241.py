from sys import stdin
import heapq

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
heapq.heapify(nums)
ans = 0

while True:
    if len(nums)==1:
        print(ans)
        break
    else:
        s1 = heapq.heappop(nums)
        s2 = heapq.heappop(nums)
        ans+=s1*s2
        heapq.heappush(nums,s1+s2)
