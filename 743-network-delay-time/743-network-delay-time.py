class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u, w, t in times:
            graph[u].append([t, w])
        print(graph)
        minHeap = [[0, k]]
        
        visited = set()
        
        time = 0
        while minHeap:
            
            t, node = heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = t # save the lowest time
            
            if node not in graph:
                continue
            for tm, v in graph[node]:
                heappush(minHeap, [time + tm, v])
                
        if len(visited) == n:
            return time
        return -1
            