class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 0:
            return None
        
        if n == 1:
            return [0]
        
        graph = {i: [] for i in range(n)}
        inDegrees = {i: 0 for i in range(n)}
        
        for edge in edges:
            edge1, edge2 = edge[0], edge[1]
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
            
            inDegrees[edge1] += 1
            inDegrees[edge2] += 1
        
        leaves = collections.deque()
        for vertex in inDegrees:
            if inDegrees[vertex] == 1:
                leaves.append(vertex)
        
        number_of_nodes = n
        while number_of_nodes > 2:
            number_of_leaves = len(leaves)
            number_of_nodes -= number_of_leaves
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                for child in graph[leaf]:
                    inDegrees[child] -= 1
                    if inDegrees[child] == 1:
                        leaves.append(child)
        
        return list(leaves)
            