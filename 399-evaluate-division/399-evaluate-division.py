class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = collections.defaultdict(list)
        
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            graph[x].append([y, value])
            graph[y].append([x, 1/value])
        
        def bfs(node1, node2):
            
            if node1 not in graph or node2 not in graph:
                return -1
            
            if node1 == node2:
                return 1
            
            visited = set()
            queue = deque()
            queue.append([node1, 1])
            
            res = -1
            while queue:
                
                node, val = queue.popleft()
                if node == node2:
                    res = val
                    return res
                
                if node in visited or node not in graph:
                    continue
                
                visited.add(node)
                for n, v in graph[node]:
                    if n not in visited and n in graph:
                        queue.append([n, v * val])
                
            return res
        
        result = []
        for n1, n2 in queries:
            result.append(bfs(n1, n2))
        
        return result
                
            