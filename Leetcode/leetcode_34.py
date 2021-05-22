class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        start=0
        end=len(nums)-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>=target:
                end=mid
            else:
                start=mid+1
                
        if nums[start]!=target:
            return [-1,-1]
        
        left=start
        right=start
        for i in range(start+1,len(nums)):
            if nums[i]==target:
                right=i
            else:
                break
        for i in range(start-1,0,-1):
            if nums[i]==target:
                left=i
        return [left,right]
