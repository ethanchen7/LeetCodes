"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        copies = {}
        
        def createNode(node):
            
            if node in copies:
                return copies[node]
            
            if not node:
                return None
            
            copy = Node(node.val)
            copies[node] = copy
            
            copy.next = createNode(node.next)
            copy.random = createNode(node.random)
            
            return copy
        
        return createNode(head)