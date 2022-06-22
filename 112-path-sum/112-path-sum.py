# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, pathSum):
            
            if not node:
                return 0
            
            pathSum += node.val
            
            if not node.left and not node.right:
                return pathSum == targetSum
            

            return (dfs(node.left, pathSum) or
            dfs(node.right, pathSum))
        
        return dfs(root, 0)