import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        dic = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
        
        temp = []
        for k,v in dic.items():
            for num in v:
                temp.append(num)
                if len(temp) == k:
                    ans.append(temp)
                    temp=[]
                
        return ans
