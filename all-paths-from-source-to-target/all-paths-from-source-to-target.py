class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj_list = {i: [] for i in range(len(graph))}
        
        for i, edge in enumerate(graph):
            for e in edge:
                adj_list[i].append(e)
        
        res = []
        path = [0]
        
        def dfs(node, path):
            
            if node == len(graph) - 1:
                res.append(path)
                return
                
            for vertex in adj_list[node]:
                new_path = path + [vertex]
                dfs(vertex, new_path)
        
        dfs(0, path)
        return res
                