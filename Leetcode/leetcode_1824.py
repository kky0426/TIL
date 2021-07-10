class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        first = 1
        second = 0
        third = 1
        
        for obs in obstacles:
            if obs == 0:
                first = min(first,second+1,third+1)
                second = min(first+1,second,third+1)
                third = min(first+1,second+1,third)
            elif obs == 1:
                first = float("INF")
                second = min(second,third+1)
                third = min(second+1,third)
            elif obs == 2:
                first = min(first,third+1)
                second = float("INF")
                third = min(first+1,third)
            elif obs == 3:
                first = min(first,second+1)
                second = min(first+1,second)
                third = float("INF")
            
        return min(first,second,third)
                
