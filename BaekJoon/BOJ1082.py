from sys import stdin

N = int(stdin.readline())
costs = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
nums = [(i,costs[i]) for i in range(N)]
nums.sort(key=lambda x:x[1])

min_num,min_cost = nums[0]
ans = [min_num]*(M//min_cost)
M = M%min_cost

nums.sort(key=lambda x:x[0],reverse=True)

idx = 0
for i in range(len(ans)):
    for j in range(N):
        if nums[j][1]<=M+min_cost:
            ans[i] = nums[j][0]
            M+=min_cost
            M-=nums[j][1]
            break

    if ans[idx] == 0:
        idx+=1
        M+=min_cost

if idx == len(ans):
    print(0)
else:
    print("".join(map(str,ans[idx:])))
