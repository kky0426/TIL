class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans = 0
        l = len(arr)
        dic = {}
        for num in arr:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        s_list = sorted(dic.items(),key=lambda x:x[1],reverse=True)
        
        for nums in s_list:
            if l<=len(arr)/2:
                break
            l-=nums[1]
            ans+=1
        return ans
                
