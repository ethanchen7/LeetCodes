# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque() 
        queue.append((root, 0)) # node, col_index
        max_width = 0
        
        while queue:
            
            length_queue = len(queue)
            _, first_index = queue[0]
            for _ in range(length_queue):
                
                node, col_idx = queue.popleft()
                
                if node.left:
                    queue.append((node.left, col_idx * 2))
                
                if node.right:
                    queue.append((node.right, col_idx * 2 + 1))
                
                max_width = max(max_width, col_idx - first_index + 1)
                
        return max_width
        