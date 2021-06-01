class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        left,right=0,0
        far=0
        
        while right<len(nums)-1:
            for i in range(left,right+1):
                far=max(far,nums[i]+i)
            left=right+1
            right=far
            ans+=1
        
        return ans     
