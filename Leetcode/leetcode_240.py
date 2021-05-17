class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        i=0
        j=col-1
        while 0<=i<row and 0<=j<col:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False
