class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pre=[]
        ans=[]
        def dfs(candidates,n):
            if sum(pre)>target:
                return
            if n==0 and sum(pre)==target:
                ans.append(pre[:])
                
            for i in range(len(candidates)):
                pre.append(candidates[i])
                dfs(candidates[i:],n-1)
                pre.pop()
        
        for i in range(target):
            dfs(candidates,i+1)
           
               
        return ans
