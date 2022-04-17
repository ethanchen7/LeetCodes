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
        self.dfs(root, [], 0, targetSum, result)
        return result
        
    def dfs(self, node, currPath, localSum, targetSum, result):
        
        if not node:
            return
        
        currPath = currPath + [node.val]
        localSum += node.val
        
        if not node.left and not node.right and localSum == targetSum:
            result.append(currPath)
        
        self.dfs(node.left, currPath, localSum, targetSum, result)
        self.dfs(node.right, currPath, localSum, targetSum, result)
        
        
        