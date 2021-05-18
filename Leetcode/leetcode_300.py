class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=len(nums)
        dp=[0]*(l+1)
        dp[1]=1
        for i in range(1,l+1):
            m_val=0
            for j in range(1,i):
                if nums[i-1]>nums[j-1]:
                    m_val=max(m_val,dp[j])
                dp[i]=m_val+1
        return max(dp)
        
