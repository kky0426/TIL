class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        l = len(nums)-1
        nums.sort()
        ans = 2000000001
        
        for i in range(4):
            for j in range(4):
                if i+j<4:
                    ans = min(ans,nums[l-j]-nums[i])
                    print(ans,i,l-j)
        return ans
