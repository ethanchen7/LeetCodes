from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {}
        
        for n in nums:
            
            if n not in nums_dict:
                nums_dict[n] = 0
            nums_dict[n] += 1
        
        maxHeap = []
        for num in nums_dict:
            heappush(maxHeap, [-nums_dict[num], num])
        
        res = []
        while k > 0:
            res.append(heappop(maxHeap)[1])
            k -= 1
        
        return res