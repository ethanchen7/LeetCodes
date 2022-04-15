# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, localSum):
            
            if not node:
                return False
            
            localSum += node.val
            
            if not node.left and not node.right and localSum == targetSum:
                return True
            
            return dfs(node.left, localSum) or dfs(node.right, localSum)

        
        return dfs(root, 0)