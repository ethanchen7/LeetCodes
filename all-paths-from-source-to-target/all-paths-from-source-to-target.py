class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj_list = {i: [] for i in range(len(graph))}
        
        for i, e in enumerate(graph):
            adj_list[i] += e
        
        queue = collections.deque()
        path = [0]
        queue.append(path)
        
        result = []
        
        while queue:
            
            current_path = queue.popleft()
            last_node = current_path[-1]
            
            for vertex in graph[last_node]:
                temp_path = current_path[:]
                temp_path.append(vertex)
                if vertex == len(graph) - 1:
                    result.append(temp_path)
                else:
                    queue.append(temp_path)
        
        return result