from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        ans=[]
        left=[]
        right=deque()
        
        for i in range(len(nums)):
            left.append(product)
            product*=nums[i]
        
        product=1
        for i in range(len(nums)-1,-1,-1):
            right.appendleft(product)
            product*=nums[i]
  
        
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
            
        return ans
