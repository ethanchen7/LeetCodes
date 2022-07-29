# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            
            if not node:
                return None
            
            if p.val <= node.val <= q.val:
                return node
            
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left)
        
            elif node.val < p.val and node.val < q.val:
                return dfs(node.right)
            
            else:
                return node
        
        return dfs(root)