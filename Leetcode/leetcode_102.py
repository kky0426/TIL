# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue=deque()
        ans=[]
        temp=[]
        queue.append((root,0))
        if not root:
            return []
        while queue:
            node,level=queue.popleft()
            temp.append((node.val,level))
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        
        level,tmp=0,[]
        for i in range(len(temp)):
            if temp[i][1] != level:
                ans.append(tmp)
                level+=1
                tmp=[]
                tmp.append(temp[i][0])
            else:
                tmp.append(temp[i][0])
        ans.append(tmp)
            
        return ans
