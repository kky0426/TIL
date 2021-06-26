class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        sorted_list = sorted(intervals,key=lambda x:x[1])
        pre = 0
        for i in range(1,len(sorted_list)):
            if sorted_list[pre][1]>sorted_list[i][0]:
                count+=1
            else:
                pre = i
        return count
