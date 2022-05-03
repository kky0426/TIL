class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_num = max(nums)
        for i in range(1,max_num):
            if i not in numset:
                return i
        if max_num<0:
            return 1
        return max_num+1