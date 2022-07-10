# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        result = []
        
        def dfs(root, pathNodes, pathSum):
            
            if not root:
                return
            
            pathSum += root.val
            pathNodes = pathNodes + [root.val]
            
            if not root.left and not root.right and pathSum == targetSum:
                result.append(pathNodes)
            
            if root.left:
                dfs(root.left, pathNodes, pathSum)
            
            if root.right:
                dfs(root.right, pathNodes, pathSum)
        
        dfs(root, [], 0)
        return result