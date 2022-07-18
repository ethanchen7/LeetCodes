# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.max_diameter = max(self.max_diameter, left + right)
            
            return max(left, right) + 1
        
        dfs(root)
        return self.max_diameter
            