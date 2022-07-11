# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.count = 0
        
        def dfs(root, pathNodes):
            
            if not root:
                return
            
            pathNodes = pathNodes + [root.val]
            
            localsum = 0
            for i in range(len(pathNodes) - 1, -1, -1):
                localsum += pathNodes[i]
                if localsum == targetSum:
                    self.count += 1
            
            dfs(root.left, pathNodes)
            dfs(root.right, pathNodes)
            
            pathNodes.pop()
            
            
        dfs(root, [])
        return self.count