# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans=[]
        def dfs(root,path):
            if not root:
                return
            path.append(root.val)
            if not(root.left or root.right):
                if sum(path)==targetSum:
                    ans.append(path[:])
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()
        
        dfs(root,[])
        return ans
