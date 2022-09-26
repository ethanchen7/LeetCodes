# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            
            if not node:
                return 0
            
            left, right = height(node.left) + 1, height(node.right) + 1
            
            return max(left, right)
        
        if not root: return True
        
        if abs(height(root.left) - height(root.right)) >= 2:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
            
            