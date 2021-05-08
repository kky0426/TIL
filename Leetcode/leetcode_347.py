class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        ans=[]
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
                
        sdic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            ans.append(sdic[i][0])
                
        return ans
        
