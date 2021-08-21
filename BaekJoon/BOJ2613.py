from sys import stdin

N,M = map(int,stdin.readline().split())

nums = list(map(int,stdin.readline().split()))

ans = 0
left = 0
right = sum(nums)

while left<=right:
    mid = left+(right-left)//2
    group = 0
    count=1
    flag = False
    for num in nums:
        if group+num <= mid:
            group+=num
        else:
            if num>mid:
                flag=True
                break
            count+=1
            group = num
    if flag:
        left = mid+1
        continue

    if count<=M:
        ans = mid
        right=mid-1
    else:
        left=mid+1


ans_list = []
total = 0
count = 0
for i in range(N):
    total+=nums[i]
    if total>ans:
        M-=1
        total=nums[i]
        ans_list.append(count)
        count=0
    count+=1
    if N-i == M:
        break

while M:
    ans_list.append(count)
    M-=1
    count=1
print(ans)
print(" ".join(map(str,ans_list)))
