class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 1
        up = [0] * len(nums)
        down = [0] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(0,i+1):
                if nums[i]-nums[j]>0:
                    up[i] = max(up[i],down[j]+1)
                elif nums[i]-nums[j]<0:
                    down[i] = max(down[i],up[j]+1)
        return max(up[-1],down[-1])+1
