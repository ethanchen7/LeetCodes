from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        minHeap = []
        
        # don't need to add more than k elements
        for i in range(min(k,len(matrix))):
            heappush(minHeap, [matrix[i][0], 0, matrix[i]])
        
        number = -1
        numberCount = 0
        while minHeap:
            
            current = heappop(minHeap)
            num, col, r = current
            
            number = num
            numberCount += 1
            if numberCount == k:
                break
            
            
            if len(r) > col + 1:
                heappush(minHeap, [r[col + 1], col + 1, r])
        
        return number