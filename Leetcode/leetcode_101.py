# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirrored(root,root)
    
    def isMirrored(self,t1:TreeNode,t2:TreeNode)->bool:
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        return (t1.val==t2.val) and self.isMirrored(t1.left,t2.right) and self.isMirrored(t1.right,t2.left)
