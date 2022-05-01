from sys import stdin
import heapq

N,M = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))
heapq.heapify(nums)

for _ in range(M):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    s = x+y
    heapq.heappush(nums,s)
    heapq.heappush(nums,s)

print(sum(nums))