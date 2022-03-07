# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # bfs
        if not root:
            return 0
        
        queue = collections.deque([root])
        
        size = 0
        while queue:
            
            size += 1

            for i in range(len(queue)):
                
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return size
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return size
                
                