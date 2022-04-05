# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        if not root: return result
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            curr_subtotal = 0
            
            for i in range(q_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                curr_subtotal += node.val
            
            avg = curr_subtotal / q_len
            result.append(avg)
        
        return result