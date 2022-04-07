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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            prevNode = None
            
            for i in range(q_len):
                currNode = queue.popleft()
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                
                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
        
        return root