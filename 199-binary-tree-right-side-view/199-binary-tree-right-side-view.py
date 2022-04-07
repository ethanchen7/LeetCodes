# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        if not root: return result 
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i == q_len - 1:
                    result.append(node.val)
        
        return result
                