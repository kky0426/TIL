from sys import stdin
import bisect
N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

search = list(set(nums))
search.sort()

for num in nums:
    idx = bisect.bisect_left(search,num)
    print(idx,end=" ")
