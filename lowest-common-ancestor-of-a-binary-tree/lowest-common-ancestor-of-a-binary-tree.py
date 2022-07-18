# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            
            if not root:
                return None
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left and right:
                return root
            
            if root.val == p.val or root.val == q.val:
                return root
            
            if left:
                return left
            elif right:
                return right
            
            return None
        
        return dfs(root, p, q)
            