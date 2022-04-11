# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        
        def dfs(node):
            
            if not node: return 0
            
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            
            return max(left, right)
        
        max_depth = dfs(root)
        return max_depth
            