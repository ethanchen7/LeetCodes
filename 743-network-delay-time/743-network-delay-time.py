class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i + 1: [] for i in range(n)}
        
        for relation in times:
            source, sink, time = relation
            graph[source].append([sink, time])
        
        minHeap = [[0, k]]
        visited = set()
        t = 0
        
        while minHeap:
            t1, node = heappop(minHeap)
            if node not in visited:
                t = t1
                visited.add(node)
                for v, t2 in graph[node]:
                    heappush(minHeap, [t2 + t1, v])
            
        if len(visited) == n:
            return t
        
        else:
            return -1