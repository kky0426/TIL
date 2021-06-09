class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[-1]
        heights.append(0)
        ans=0
        for i in range(len(heights)):
            h = heights[i] #i번째 높이
            
            while stack[-1]!=-1 and heights[stack[-1]]>=h:
                target = stack.pop()
                right = i
                left = stack[-1]
                S = heights[target] * (right-left-1)
                ans=max(ans,S)
            stack.append(i)
            
        return ans
