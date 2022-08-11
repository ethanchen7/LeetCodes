class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = {i: [] for i in range(n)}
        for s, d, e in flights:
            graph[s].append([e, d])
        
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        
        minHeap = [[0, 0, src]] # cost, k, node
        
        while minHeap:
            
            cst, curr_k, node = heappop(minHeap)
            # print(cst, curr_k, node)
            if node == dst:
                return cst
            
            if curr_k == k + 1:
                continue
            
            for c, n in graph[node]:
                
                if cst + c < distances[n]: # we found a cheaper cost to that node
                    distances[n] = cst + c
                    heappush(minHeap, [cst + c, curr_k + 1, n])
                    current_stops[n] = curr_k
                
                # we didn't find a cheaper cost, but we still have more stops to check,
                # we should still keep going in case we find an overall better cost
                elif curr_k < current_stops[n]: 
                    heappush(minHeap, [cst + c, curr_k + 1, n])
        
        return -1 if distances[dst] == float("inf") else distances[dst]