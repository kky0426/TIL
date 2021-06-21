class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #newList = []
        ans = [0,0,0]
        for trip in triplets:
            if trip[0]>target[0] or trip[1]>target[1] or trip[2]>target[2]:
                continue
            else:
                for i in range(3):
                    ans[i]=max(ans[i],trip[i])
            if ans == target:
                return True
        return False
