# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = collections.deque()
        if not root:
            return result
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            curr_subarr = []
            for i in range(q_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                curr_subarr.append(node.val)
            
            result.appendleft(curr_subarr)
        
        return result