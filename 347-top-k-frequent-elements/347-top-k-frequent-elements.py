class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        
        maxHeap = []
        for key in num_map:
            heappush(maxHeap,(-num_map[key], key))
        
        res = []
        for i in range(k):
            freq, num = heappop(maxHeap)
            res.append(num)
        
        return res