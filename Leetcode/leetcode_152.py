class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        ans = nums[0]
        
        for i in range(1,len(nums)):
            temp_max = cur_max*nums[i]
            temp_min = cur_min*nums[i]
            
            cur_max = max(temp_max,max(temp_min,nums[i]))
            cur_min = min(temp_min,min(temp_max,nums[i]))
            
            ans=max(ans,cur_max)
            
        return ans
