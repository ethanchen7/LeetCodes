class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        
        def less_than_k(mid):
            count = 0
            
            for r in range(n):
                x = bisect_right(matrix[r], mid) # all the numbers less than K
                count += x
            
            return count
        
        while start < end:
            
            mid = start + (end - start) // 2
            if less_than_k(mid) < k:
                start = mid + 1
            else:
                end = mid
            
        return start