class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        s = sum(nums)
        left = 0
        right = s
        
        for i in range(len(nums)):
            left +=nums[i]
            right -=nums[i]
            ans.append( (nums[i]*(i+1)-left) + right-nums[i]*(len(nums)-i-1) )
        return ans
