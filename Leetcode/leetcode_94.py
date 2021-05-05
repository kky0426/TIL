# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        
        def travel(root):
            if root:
                if root.left != None:
                    travel(root.left)
                ans.append(root.val)
                if root.right != None:
                    travel(root.right)
        travel(root)
        return ans
    
