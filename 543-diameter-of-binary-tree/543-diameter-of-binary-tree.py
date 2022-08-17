# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        
        def dfs(node):
            
            nonlocal diameter
            
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 0
            
            left, right = 0, 0
            if node.left:
                left = 1 + dfs(node.left)
            
            if node.right:
                right = 1 + dfs(node.right)
            
            localDiam = left + right
            
            diameter = max(localDiam, diameter)
            
            return max(left, right)
        
        dfs(root)
        return diameter