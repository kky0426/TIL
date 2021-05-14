class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        water=0
        while start<=end:
            temp=(end-start)*min(height[start],height[end])
            water=max(water,temp)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return water
        
