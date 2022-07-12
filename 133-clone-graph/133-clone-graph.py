"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        clone_graph = {}
        
        def dfs(node):
            
            if node in clone_graph:
                return clone_graph[node]
            
            copy = Node(node.val)
            clone_graph[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)