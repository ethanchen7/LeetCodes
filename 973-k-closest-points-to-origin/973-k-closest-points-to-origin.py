from heapq import *
from math import *
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        res = []
        
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapify(minHeap)
        
        while k > 0:
            distance, x, y = heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res