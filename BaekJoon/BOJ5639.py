from sys import stdin
import sys
sys.setrecursionlimit(10**6)
preoder = []

while True:
    try:
        preoder.append(int(stdin.readline()))
    except:
        break

def get_postoder(nums):
    N = len(nums)
    if N<=1:
        return nums

    for i in range(1,N):
        if nums[i]>nums[0]:
            return get_postoder(nums[1:i])+get_postoder(nums[i:]) + [nums[0]]

    return get_postoder(nums[1:])+[nums[0]]

postoder = get_postoder(preoder)
for node in postoder:
    print(node)
