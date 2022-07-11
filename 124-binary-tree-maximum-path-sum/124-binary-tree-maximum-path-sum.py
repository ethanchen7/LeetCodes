# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max_sum = -999999
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            
            temp_max = root.val + leftMax + rightMax
            self.max_sum = max(temp_max, self.max_sum)
            
            return max(leftMax, rightMax) + root.val
        
        dfs(root)
        return self.max_sum