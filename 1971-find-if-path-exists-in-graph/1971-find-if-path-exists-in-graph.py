class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = {i: [] for i in range(n)}
        for edge in edges:
            n1, n2 = edge
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            if node == destination:
                return True
            
            visited.add(node)
            
            for vertex in graph[node]:
                result = dfs(vertex)
                if result == True:
                    return True
        
            return False

        return dfs(source)
        