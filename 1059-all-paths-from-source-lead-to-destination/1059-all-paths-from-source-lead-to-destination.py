class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i: [] for i in range(n)}
        
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)
        
        seen = set()
        def dfs(v):
            
            if len(graph[v]) == 0:
                return v == destination
            
            if v in seen: #cycle detected
                return False
            
            seen.add(v)
            
            for node in graph[v]:
                res = dfs(node)
                if not res:
                    return False
                
            seen.remove(v)
            return True
        
        return dfs(source)
                