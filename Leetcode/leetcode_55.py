class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        idx=last-1
        while idx>=0:
            if idx+nums[idx]>=last:
                last=idx
                idx-=1
            else:
                idx-=1
        
        return last==0
