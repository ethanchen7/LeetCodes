# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        output = []
        
        if not root:
            return output
        
        def dfs(node):
            
            if not node: return
            
            output.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return output