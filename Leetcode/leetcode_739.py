class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans=[0]*len(T)
        stack=[]
        stack.append(0)
        for idx in range(1,len(T)):
            while stack and T[idx]>T[stack[-1]]:
                last_idx=stack.pop()
                ans[last_idx]=idx-last_idx
            stack.append(idx)
        return ans
