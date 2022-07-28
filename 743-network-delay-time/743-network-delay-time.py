class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i + 1: [] for i in range(n)}
        
        for u, v, w in times:
            graph[u].append([w, v])
        
        minHeap = [[0, k]]
        visited = set()
        
        time = 0
        
        while minHeap:
            
            t, v = heappop(minHeap)
            if v not in visited:
                time = t
                visited.add(v)
                
                for t2, node in graph[v]:
                    heappush(minHeap, [time + t2, node])
        
        if len(visited) == n:
            return time
        
        return -1
            