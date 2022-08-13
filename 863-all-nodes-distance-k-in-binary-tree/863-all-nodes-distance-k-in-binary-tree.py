# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # this approach is similar to a graph, traverse the neighbors up to K distance
        # mark all the parents of each node so that we can have direct access to them
        parents = {}
        def dfs(node, parent=None):
            
            if not node:
                return
            
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        result = []
        queue = deque([(target, 0)]) # bfs from target for all nodes K distance away
        visited = set()
    
        while queue:
            
            node, distance = queue.popleft()
            
            if distance == k and node not in visited:
                return [node.val] + [n.val for n, d in queue] 
            # we can just append all of them onto the queue bc they are all distance K at this point of the queue
            
            if node not in visited:
                visited.add(node)
                
                for neighbor in [node.left, node.right, parents[node]]:
                    
                    if neighbor and neighbor not in visited:
                        queue.append((neighbor, distance + 1))
        
        return result