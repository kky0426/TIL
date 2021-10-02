from sys import stdin

N,K = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))

left = 0
right = 0
ans = float("inf")
dic = {1:0,2:0}

while right<N+1:
    if dic[1]>=K:
        ans = min(ans,right-left)
        dic[nums[left]]-=1
        left+=1
    else:
        if right>=N: break
        dic[nums[right]]+=1
        right+=1

print(ans if ans != float("inf") else -1)
