class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for num in position:
            if num%2 == 0:
                even+=1
            else:
                odd+=1
        return min(even,odd)
