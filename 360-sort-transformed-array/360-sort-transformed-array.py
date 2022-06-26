class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        minHeap = []
        res = []
        
        for n in nums:
            heappush(minHeap, self.quadratic(n, a, b, c))
        
        for i in range(len(minHeap)):
            res.append(heappop(minHeap))
        
        return res
        
    def quadratic(self, x, a, b, c):
        return ((a * x * x) + (b * x) + c)