# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, pathMax):
            
            if not node:
                return 0
            
            if node.val >= pathMax:
                return 1 + dfs(node.left, max(pathMax, node.val)) + dfs(node.right, max(pathMax, node.val))
            
            return dfs(node.left, max(pathMax, node.val)) + dfs(node.right, max(pathMax, node.val))
        
        return dfs(root, root.val)