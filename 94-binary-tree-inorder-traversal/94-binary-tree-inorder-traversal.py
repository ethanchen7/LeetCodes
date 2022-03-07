# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        output = []
        
        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            output.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return output