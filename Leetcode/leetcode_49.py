class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_list=[]
        ans=[]
        visit=[0]*len(strs)
        for word in strs:
            dic={}
            for alpha in word:
                if alpha in dic:
                    dic[alpha]+=1
                else:
                    dic[alpha]=1
            dic_list.append(dic)
            
        for i in range(len(strs)):
            temp=[]
            if visit[i]==0:
                temp.append(strs[i])
            for j in range(i+1,len(strs)):
                if dic_list[i]==dic_list[j]:
                    if visit[j]==0:
                        visit[j]=1
                        temp.append(strs[j])
            if temp:
                ans.append(temp)
    
        return ans
