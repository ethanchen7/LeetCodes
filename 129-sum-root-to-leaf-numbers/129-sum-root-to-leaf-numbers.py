# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        return self.dfs(root, 0, total)
        
        
        
    def dfs(self, node, currNum, total):
        
        if not node:
            return 0
        
        currNum = currNum * 10 + node.val
        
        if not node.left and not node.right:
            total += currNum
            return total
        
        return self.dfs(node.left, currNum, total) + self.dfs(node.right, currNum, total)