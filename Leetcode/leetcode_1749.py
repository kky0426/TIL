class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_dp=[0]*(len(nums)+1)
        max_dp=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            min_dp[i]=min(nums[i-1],min_dp[i-1]+nums[i-1])
            max_dp[i]=max(nums[i-1],max_dp[i-1]+nums[i-1])
        
        max_num = max(max_dp)
        min_num = min(min_dp)
        return max(max_num,-min_num)
