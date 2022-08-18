class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: set() for i in range(n)}
        
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        visited = set()
        def dfs(stack):
            
            while stack:
                
                node = stack.pop()
                visited.add(node)
                
                for neighbor in graph[node]:
                    
                    if neighbor in visited:
                        continue
                    
                    stack.append(neighbor)
                    graph[neighbor].remove(node) 
                    # remove the edge going back to the parent so we don't visit it again
        
        components = 0
        for i in range(n):
            
            if i not in visited:
                dfs([i])
                components += 1
        
        return components
                    
            
            