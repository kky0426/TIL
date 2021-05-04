"""
#itertools 풀이
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums,len(nums)))
"""

#dfs 풀이
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        ans=[]
        pre=[]
        def dfs(nums):
            if len(nums)==0:
                ans.append(pre[:])
            for i in range(len(nums)): 
                next=nums[:i]+nums[i+1:]
                pre.append(nums[i])
                dfs(next)
                pre.pop()
        dfs(nums)
        return ans
