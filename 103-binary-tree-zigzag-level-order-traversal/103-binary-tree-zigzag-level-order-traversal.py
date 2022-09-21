# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return None
        
        queue = deque([root])
        
        result = []
        reverse = False
        
        while queue:
            
            level_arr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                
                level_arr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if reverse:
                result.append(level_arr[::-1])
            else:
                result.append(level_arr)
            
            reverse = not reverse
        
        return result