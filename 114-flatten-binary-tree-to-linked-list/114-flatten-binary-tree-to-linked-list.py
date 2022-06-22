# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        stack = []
        if root:
            stack.append(root)
            
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
            if stack:
                next_right = stack[-1]
                node.right = next_right
                node.left = None