class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        
        for num in arr:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
                
        sorted_dic=sorted(dic.items(),key= lambda x : x[1],reverse=True)
        while k>0:
            k-=sorted_dic[-1][1]
            sorted_dic.pop()
        if k==0:
            return len(sorted_dic)
        else:
            return len(sorted_dic)+1
