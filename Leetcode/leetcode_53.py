class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-10001]*(len(nums)+1)
        if len(nums)==1:
            return nums[0]
        
        for i in range(1,len(nums)+1):
            dp[i]=max(nums[i-1],dp[i-1]+nums[i-1])
        return max(dp)
