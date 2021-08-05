from sys import stdin

N,K = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().rstrip()))

stack=[]

count=0
for i in range(len(nums)):
    while stack and stack[-1]<nums[i] and count!=K:
        stack.pop()
        count+=1
    stack.append(nums[i])

if count<K:
    for _ in range(K-count):
        stack.pop()
        
print("".join(map(str,stack)))
