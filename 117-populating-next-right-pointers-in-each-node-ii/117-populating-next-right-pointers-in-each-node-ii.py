"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue = collections.deque()
        if not root:
            return None
        
        queue.append(root)
        
        while queue:
            
            prevNode = None
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                if prevNode:
                    prevNode.next = node
                    
                prevNode = node
                
            prevNode.next = None
        
        return root