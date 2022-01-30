from collections import defaultdict
import copy
def solution(info, edges):

    N = len(info)
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
    ans = 0
    
    def solve(cur,sheep,wolf,nodes):
        if info[cur] == 0:
            sheep+=1
        else:
            wolf+=1
     
        if sheep<=wolf:
            return
        else:
            nonlocal ans
            ans = max(ans,sheep)
        
        temp = copy.deepcopy(nodes)
        idx = temp.index(cur)
        temp.pop(idx)
        
        for n in graph[cur]:
            temp.append(n)
     
        for next_node in temp:
            solve(next_node,sheep,wolf,temp)
 

    solve(0,0,0,[0])
    return ans
