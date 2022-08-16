class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        
        minHeap = []
        
        for i in range(min(k, len(matrix))):
            heappush(minHeap, [matrix[i][0], i, 0])
        
        numberCount = 0
        number = None
        
        while minHeap:
            
            number, curr_row, curr_col = heappop(minHeap)
            numberCount += 1
            
            if numberCount == k:
                break
                
            if curr_col < n - 1:
                heappush(minHeap, [matrix[curr_row][curr_col + 1], curr_row, curr_col + 1])
            
        return number