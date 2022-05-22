from sys import stdin

N,K = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

count = [0]*101
for n in nums:
    count[n]+=1

queue = []
ans = 0
for i in range(len(nums)):
    if nums[i] in queue:
        count[nums[i]]-=1
        continue
    if len(queue)<N:
        count[nums[i]]-=1
        queue.append(nums[i])
        continue

    idx = -1
    for j in queue:
        if count[j] == 0:
            idx = j
            break
    if idx != -1:
        queue[queue.index(idx)] = nums[i]
        count[nums[i]]-=1
        ans+=1
        continue

    last = 0
    value = 0
    for q in queue:
        if last < nums[i:].index(q):
            last = nums[i:].index(q)
            value = q
    queue[queue.index(value)] = nums[i]
    count[nums[i]]-=1
    ans+=1

print(ans)

