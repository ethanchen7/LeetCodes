"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        clones = {}
        
        def dfs(node):
            
            if not node:
                return None
            
            if node in clones:
                return clones[node]
        
            copy = Node(node.val)
            clones[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)