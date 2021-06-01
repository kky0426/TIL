class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visit=[0]*len(arr)
        
        def dfs(idx):
            if idx < 0 or idx>=len(arr):
                return
            
            if visit[idx]==1:
                return
            
            if arr[idx] == 0 :
                return True
            visit[idx]=1
            return dfs(idx+arr[idx]) or dfs(idx-arr[idx])
        return dfs(start)
