# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result= []
        def dfs_right(node, level):
            
            if level == len(result): # check that we're on the next level
                result.append(node.val)
            
            for child in [node.right, node.left]: # keep going right
                if child:
                    dfs_right(child, level + 1)
        
        
        if not root: 
            return result
        dfs_right(root, 0)
        return result
                    
        