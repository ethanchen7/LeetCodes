# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        allPaths = []
        
        def dfs(node, currPath, currSum):
            
            currSum += node.val
            currPath = currPath + [node.val]
            
            if node.left:
                dfs(node.left, currPath, currSum)
            
            if node.right:
                dfs(node.right, currPath, currSum)
            
            if not node.left and not node.right and currSum == targetSum:
                allPaths.append(currPath)
        
        if not root: return allPaths
        dfs(root, [], 0)
        return allPaths