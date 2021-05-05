#backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(fst,cur,n):
            if len(cur)==n:
                ans.append(cur[:])
                return
            for i in range(fst,len(nums)):
                cur.append(nums[i])
                backtracking(i+1,cur,n)
                cur.pop()
        ans=[]
        for k in range(len(nums)+1):
            cur=[]
            backtracking(0,cur,k)
        return ans
    

""" itertool 
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(nums)+1):
            ans.extend(list(combinations(nums,i)))
        return ans

"""
