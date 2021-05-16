# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag=False
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return self.flag
        def dfs(root,n):
            if not root:
                return
            n+=root.val
            if not (root.left or root.right):
                if n==targetSum:
                    self.flag=True
            dfs(root.left,n)
            dfs(root.right,n)
        
        dfs(root,0)
        return self.flag
