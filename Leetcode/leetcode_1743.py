import collections
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        dic=collections.defaultdict(list)
        for i,j in adjacentPairs:
            dic[i].append(j)
            dic[j].append(i)
        
        for k,v in dic.items():
            if len(v)==1:
                start = k
                break
        
        visit = set()
        def dfs(num):
            ans.append(num)
            visit.add(num)
            for i in dic[num]:
                if i not in visit:
                    dfs(i)
        dfs(start)
        return ans
