from sys import stdin

N= int(stdin.readline())

nums=list(map(int,stdin.readline().split()))
nums.sort()

target = 1

for num in nums:
    if target<num:
        break
    target+=num

print(target)
