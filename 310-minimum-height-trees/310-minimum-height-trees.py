class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # remove all the leaf nodes and prune their edges
        # keep repeating that until you are left with 1 or 2 nodes 
        # the answer to the hint in LC is that you can only have a max of 1-2 MHTs
        
        if n <= 1:
            return [0]
        
        graph = {i: [] for i in range(n)}
        inDegrees = {i: 0 for i in range(n)}
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
            inDegrees[x] += 1
            inDegrees[y] += 1
        
        leaves = deque()
        for node in inDegrees:
            if inDegrees[node] == 1:
                leaves.append(node)
        
        totalNodes = n
        while totalNodes > 2:
            leaf_count = len(leaves)
            totalNodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for node in graph[leaf]:
                    inDegrees[node] -= 1
                    if inDegrees[node] == 1:
                        leaves.append(node)
        
        return list(leaves)