from sys import stdin
from math import ceil

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
speed = nums[N-1]

for i in range(N-2,-1,-1):
    speed = ceil(speed/nums[i])*nums[i]

print(speed)