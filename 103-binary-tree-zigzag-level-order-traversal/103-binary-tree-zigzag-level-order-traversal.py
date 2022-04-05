# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if not root: return result
        
        queue = collections.deque()
        queue.append(root)
        
        reverse = False
        while queue:
            
            q_len = len(queue)
            curr_subarr = collections.deque()
            
            for i in range(q_len):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if reverse:
                    curr_subarr.appendleft(node.val)
                else:
                    curr_subarr.append(node.val)
            
            reverse = not reverse
            result.append(list(curr_subarr))
        
        return result
            