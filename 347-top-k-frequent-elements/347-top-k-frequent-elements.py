from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        maxHeap = []
        
        for n in nums:
            if n not in frequency:
                frequency[n] = 0
            frequency[n] += 1
        
        for num in frequency:
            heappush(maxHeap, [-frequency[num], num])
        
        res = []
        while k > 0:
            freq, num = heappop(maxHeap)
            res.append(num)
            k -= 1
        
        return res