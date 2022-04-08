# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        allPaths = []
        
        def dfs(node, currPath):
            
            if not node: return ""
            
            currPath += str(node.val)
            
            if node.left:
                dfs(node.left, currPath + "->")
            
            if node.right:
                dfs(node.right, currPath + "->")
            
            if not node.left and not node.right:
                allPaths.append(currPath)
        
        dfs(root, "")
        return allPaths    