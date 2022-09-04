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
        def dfs(node, path, total):
            
            if not node:
                return
            
            if not node.left and not node.right:
                if (total + node.val) == targetSum:
                    result.append(path + [node.val])
                return
            
            dfs(node.left, path + [node.val], total + node.val)
            dfs(node.right, path + [node.val], total + node.val)
            
        
        dfs(root, [], 0)
        return result