# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.p_found = False
        self.q_found = False
        
        def helper(node):
            
            if not node:
                return
            
            left = helper(node.left)
            right = helper(node.right)
            
            if node.val == p.val:
                self.p_found = True
                return node
            
            if node.val == q.val:
                self.q_found = True
                return node
            
            if left and right:
                return node
            
            elif left:
                return left
            
            elif right:
                return right
            
            return
        
        result = helper(root)
        if self.p_found and self.q_found:
            return result
        return None