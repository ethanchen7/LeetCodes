class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        
        maxHeap = []
        
        for key in num_map:
            maxHeap.append((-num_map[key], key)) # O(N)
        
        heapify(maxHeap) # O(N)
        
        res = []
        for i in range(k): # O(K log K)
            freq, num = heappop(maxHeap)
            res.append(num)
        
        return res
    # overall: O(N * K log K) ==== O(N * log K)