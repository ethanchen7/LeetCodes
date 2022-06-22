# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.prev = self.first_bad = self.second_bad = None
        
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            
            if self.prev and not self.first_bad and self.prev.val >= node.val:
                self.first_bad = self.prev
            
            if self.prev and self.first_bad and self.prev.val >= node.val:
                self.second_bad = node
            
            self.prev = node
            
            dfs(node.right)
            
        
        dfs(root)
        self.first_bad.val, self.second_bad.val = self.second_bad.val, self.first_bad.val