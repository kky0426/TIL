class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for key,value in dic.items():
            if value == 1:
                return key
