class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort(key=lambda x:x[0])
        
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            if start<=ans[-1][1]:
                ans[-1][1]=max(end,ans[-1][1])
            else:
                ans.append(intervals[i])
        
        return ans
            
