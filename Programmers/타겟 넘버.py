
def solution(numbers, target):
    answer = 0
    def dfs(nums,count):
        if not nums:
            if count == target:
                nonlocal answer
                answer+=1
            return        
        dfs(nums[1:],count+nums[0])
        dfs(nums[1:],count-nums[0])
    dfs(numbers,0)
    return answer
