# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        reverse = False
        result = []
        
        if not root:
            return result
        
        queue = collections.deque([root])
        while queue:
            temp_arr = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if reverse:
                    temp_arr.appendleft(node.val)
                else:
                    temp_arr.append(node.val)
                    
            
            reverse = not reverse
            result.append(list(temp_arr))
        
        return result