# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer=0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.get_h(root)
        return self.answer
        
        
    def get_h(self,root: TreeNode) -> int:
        if not root:
            return 0
        left=self.get_h(root.left)
        right=self.get_h(root.right)
        self.answer=max(self.answer,right+left)
        return 1+max(left,right)
