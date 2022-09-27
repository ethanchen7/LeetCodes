class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapify(heap)
        
        while len(heap) > 1:
            
            stone1 = heappop(heap)
            stone2 = heappop(heap)
            
            smashed = abs(abs(stone1) - abs(stone2))
            heappush(heap, -smashed)
        
        return abs(heap[-1]) if heap else 0