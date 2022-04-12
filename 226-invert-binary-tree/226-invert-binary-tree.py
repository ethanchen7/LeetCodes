# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        
        tempLeft = root.left
        tempRight = root.right
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        root.left = tempRight
        root.right = tempLeft
        
        return root