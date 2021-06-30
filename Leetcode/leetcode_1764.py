class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        ans = []
        end = 0
        for sub in groups:
            for i in range(end,len(nums)):
                if nums[i:i+len(sub)] == sub:
                    end = i+len(sub)
                    ans.append(end)
                    break
        if len(ans) == len(groups):
            return True
        else:
            return False
