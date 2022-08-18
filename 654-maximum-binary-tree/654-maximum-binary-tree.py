# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(nums):
            
            if not nums:
                return None
            
            max_num = 0
            max_idx = 0
            for i, n in enumerate(nums):
                if n > max_num:
                    max_num = n
                    max_idx = i
            
            root = TreeNode(max_num)
            root.left = dfs(nums[0: max_idx])
            root.right = dfs(nums[max_idx + 1:])
            
            return root
        
        return dfs(nums)