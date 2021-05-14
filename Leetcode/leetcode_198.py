class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        dp=[0]*(len(nums)+1)
        dp[1]=nums[0]
        dp[2]=nums[1]
        
        for i in range(3,len(nums)+1):
            dp[i]=max(dp[i-2],dp[i-3])+nums[i-1]
        return max(dp)
