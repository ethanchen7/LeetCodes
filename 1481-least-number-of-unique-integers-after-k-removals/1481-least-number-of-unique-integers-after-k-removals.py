from heapq import *
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_frequency = {}
        minHeap = []
        for n in arr:
            if n not in num_frequency:
                num_frequency[n] = 0
            num_frequency[n] += 1
        
        for num in num_frequency:
            heappush(minHeap, [num_frequency[num], num])
        
        while k > 0:
            number = heappop(minHeap)
            while number[0] > 0 and k > 0:
                number[0] -= 1
                k -= 1
            if number[0] > 0 and k < 1:
                heappush(minHeap, [number[0], number[1]])
        
        return len(minHeap)