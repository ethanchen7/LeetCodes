# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = 0
        
        def dfs(node, path):
            
            nonlocal count
            
            if not node:
                return
            
            path.append(node.val)
            localSum = 0
            for i in range(len(path) - 1, -1,- 1):
                localSum += path[i]
                if localSum == targetSum:
                    count += 1
                    
            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop()
            
        
        dfs(root, [])
        return count