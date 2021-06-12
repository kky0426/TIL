class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r = len(nums)-1
        ans = 0
        while l<r:
            pair = nums[l]+nums[r]
            ans = max(ans,pair)
            l+=1
            r-=1
            
        return ans
            
