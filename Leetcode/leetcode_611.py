class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(2,len(nums)):
            left = 0
            right = i-1
            while left<right:
                if nums[i]<nums[left]+nums[right]:
                    ans+=right-left
                    right-=1
                else:
                    left+=1
        return ans
        
