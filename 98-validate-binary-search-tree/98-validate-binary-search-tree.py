# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to check for min and max values in left and right subtrees
        
        return self.validate(root, -math.inf, math.inf)
        
    
    def validate(self, root, min_val, max_val):
        if not root:
            return True
        
        if not min_val < root.val < max_val:
            return False
        
        left = self.validate(root.left, min_val, root.val)
        right = self.validate(root.right, root.val, max_val)
        
        return left and right