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
            
            level_arr = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if reverse:
                    level_arr.appendleft(node.val)
                else:
                    level_arr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level_arr))
            
            reverse = not reverse
        
        return result