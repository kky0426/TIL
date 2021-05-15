class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic={0:0,1:0,2:0}
        for num in nums:
            dic[num]+=1
        idx=0
        for key,value in dic.items():
            for _ in range(value):
                nums[idx]=key
                idx+=1
