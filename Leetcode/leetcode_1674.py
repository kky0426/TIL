class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            count = 0
            j = 0
            while j<len(boxes):
                if boxes[j] == '1':
                    count =count + abs(i-j)
                j+=1
            ans.append(count)
        
        return ans
