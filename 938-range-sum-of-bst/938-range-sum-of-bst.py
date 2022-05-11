# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.output = 0
        
        def dfs(node):
            
            if node.val >= low and node.val <= high:
                self.output += node.val
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return self.output
            