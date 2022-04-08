# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, pathSum):
            
            if not node: return 0
            
            pathSum = pathSum * 10 + node.val
            
            if not node.left and not node.right:
                return pathSum
            
            return dfs(node.left, pathSum) + dfs(node.right, pathSum)
    
        return dfs(root, 0)