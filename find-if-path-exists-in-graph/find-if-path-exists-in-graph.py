class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = collections.defaultdict(list)
        
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()
        
        def dfs(vertex):
            
            if vertex in visited:
                return False
            
            if vertex == destination:
                return True
            
            visited.add(vertex)
            
            for node in graph[vertex]:
                result = dfs(node)
                if result:
                    return True
            

        
        return dfs(source)
        