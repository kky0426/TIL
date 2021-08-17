from sys import stdin

N,S = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))

left=0
right=0
ans=float("inf")

s = 0
while True:
    if s>=S:
        ans = min(ans,right-left)
        s-=nums[left]
        left+=1
    elif right==N:
        break
    else:
        s+=nums[right]
        right+=1


print(ans if ans!=float("inf") else 0)
