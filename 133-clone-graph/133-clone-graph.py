"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        clone = {}
        
        if not node:
            return None
        
        def dfs(node):
            
            if node in clone:
                return clone[node]
            
            copy = Node(node.val)
            clone[node] = copy
            
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            
            return copy
        
        return dfs(node)
            