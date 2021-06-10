class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ans=[]
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            matrix[i] = list(map(int,matrix[i]))
            
        #높이를 누적해서 matrix 변환
        for i in range(row):
            for j in range(col):
                if i>0:
                    if matrix[i][j] == 1:
                        matrix[i][j] = matrix[i-1][j]+1
            
        #히스토그램에서 가장 넓은 사각형 구하기
        def RectangleArea(heights):
            heights.append(0)
            stack=[-1]
            maxS = 0
            for i in range(len(heights)):
                h = heights[i]
                while stack[-1]!=-1 and heights[stack[-1]]>=h:
                    target = stack.pop()
                    left = stack[-1]
                    right = i
                    S = heights[target] * (right-left-1)
                    maxS = max(maxS,S)
                stack.append(i)
            return maxS
        #각 row 마다 최대 사각형 구하기
        for i in range(len(matrix)):
            ans.append(RectangleArea(matrix[i]))
        return max(ans)
