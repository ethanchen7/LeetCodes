# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.dfs(root, "", result)
        return result
    
    def dfs(self, node, currPath, result):
        
        if not node:
            return
        
        currPath = currPath + str(node.val) + "->"
        
        if not node.left and not node.right:
            currPath = currPath[:-2]
            result.append(currPath)
        
        self.dfs(node.left, currPath, result)
        self.dfs(node.right, currPath, result)