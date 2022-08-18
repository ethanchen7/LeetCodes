class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        graph = {i: set() for i in range(n)}
        
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        stack = [0]
        
        seen = set()
        seen.add(0)
        
        while stack:
            
            node = stack.pop()
            
            for neighbor in graph[node]:
                
                if neighbor in seen:
                    return False
                
                stack.append(neighbor)
                seen.add(neighbor)
                graph[neighbor].remove(node)
            
        return len(seen) == n
                