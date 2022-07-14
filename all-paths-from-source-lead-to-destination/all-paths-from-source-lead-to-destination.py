class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i: [] for i in range(n)}
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)

        visited = set()
        def dfs(v):
            
            if len(graph[v]) == 0:
                return v == destination
            
            if v in visited:
                return False
            
            visited.add(v)
            for vertex in graph[v]:
                res = dfs(vertex)
                if not res: 
                    return False
            
            visited.remove(v)
            
            return True
        
        return dfs(source)
        
            