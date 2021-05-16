# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    count=0
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        def dfs(root,n):
            if not root:
                return
            n+=root.val
            if n==targetSum:
                self.count+=1
            dfs(root.left,n)
            dfs(root.right,n)
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            dfs(node,0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return self.count
