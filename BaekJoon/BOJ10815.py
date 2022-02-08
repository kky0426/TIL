from sys import stdin

N = int(stdin.readline())
cards = set(map(int,stdin.readline().split()))
M = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))


for i in nums:
    if i in cards:
        print(1,end=" ")
    else:
        print(0,end=" ")
