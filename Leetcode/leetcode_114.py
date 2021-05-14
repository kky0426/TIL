# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def convert(root):
            if not root:
                return
            
            convert(root.left)
            temp=root.right
            root.right=root.left
            root.left=None
            
            tail=root
            while tail.right:
                tail=tail.right
            tail.right=temp
            convert(root.right)
        convert(root)
