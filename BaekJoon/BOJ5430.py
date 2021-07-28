from sys import stdin
from collections import deque

T=int(stdin.readline())

for _ in range(T):
    func = stdin.readline().rstrip()
    N=int(stdin.readline())
    nums=deque(stdin.readline().rstrip()[1:-1].split(","))
    if N==0:
        nums=deque()
    d=func.count('D')
    if d>N:
        print("error")
        continue
    d=0
    for com in func:
        if com=='R':
            d+=1
        elif com=='D':
            if d%2==0:
                nums.popleft()
            else:
                nums.pop()
    if d%2==0:
        nums=list(map(int,nums))
    else:
        nums=list(map(int,nums))[::-1]
    print("[",end='')
    for i in range(len(nums)):
        if i==len(nums)-1:
            print(nums[i],end='')
        else:
            print(nums[i],end=',')
    print("]")
