# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.nodes = []
        
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            self.nodes.append(node)
            dfs(node.right)
        
        dfs(root)
        
        sorted_nodes = sorted(node.val for node in self.nodes)
        
        for i in range(len(sorted_nodes)):
            if self.nodes[i] != sorted_nodes[i]:
                self.nodes[i].val = sorted_nodes[i]
        