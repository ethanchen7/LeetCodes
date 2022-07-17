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
            temp_q = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if reverse:
                    temp_q.appendleft(node.val)
                else:
                    temp_q.append(node.val)
            
            result.append(list(temp_q))
            reverse = not reverse
        
        return result