# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return 0
            
            def lheight(root):
                if not root: return 0
                return 1 + lheight(root.left)
            
            def rheight(root):
                if not root: return 0
                return 1 + rheight(root.right)
            
            left, right = lheight(root), rheight(root)
            
            if left == right:
                return (2**left) - 1
            else:
                return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        return dfs(root)