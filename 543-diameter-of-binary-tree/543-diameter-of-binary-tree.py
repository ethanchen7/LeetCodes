# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_diameter = 0
        
        def dfs(node):
            
            if not node: 
                return 0
            
            leftHeight = dfs(node.left)            
            rightHeight = dfs(node.right)
            
       
            self.max_diameter = max(self.max_diameter, leftHeight + rightHeight)
                
            return max(leftHeight, rightHeight) + 1
            
        
        res = dfs(root)
        return self.max_diameter