class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj_list = {i : graph[i] for i in range(len(graph))}
        result = []
        
        visited = set()
        def dfs(node, path):
            
            # visited.add(node)
            path = path + [node]
            
            if node == len(graph) - 1:
                result.append(path)
                return
                
            for vertex in adj_list[node]:
                dfs(vertex, path)
            
        dfs(0, [])
        return result
               