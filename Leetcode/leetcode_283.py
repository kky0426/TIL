class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        count=0
        for i in nums:
            if i==0:
                count+=1
            else:
                temp.append(i)
        
        for j in range(count):
            temp.append(0)
            
        for k in range(len(nums)):
            nums[k]=temp[k]
