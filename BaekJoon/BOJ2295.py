from sys import stdin

N = int(stdin.readline())

nums = [int(stdin.readline()) for _ in range(N)]

nums.sort()

arr = []
for i in range(N):
    for j in range(i,N):
        arr.append(nums[i]+nums[j])

arr.sort()


def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return True
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return False

ans = 0
for i in range(N):
    for j in range(i,N):
        if binary_search(arr,nums[j]-nums[i]):
            ans = max(ans,nums[j])

print(ans)
