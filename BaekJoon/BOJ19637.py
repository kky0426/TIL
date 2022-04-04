from sys import stdin
import bisect

N,M = map(int,stdin.readline().split())

titles = []
nums = []

for _ in range(N):
    title,num = stdin.readline().split()
    titles.append(title)
    nums.append(int(num))

for _ in range(M):
    power = int(stdin.readline())
    idx = bisect.bisect_left(nums,power)
    print(titles[idx])
