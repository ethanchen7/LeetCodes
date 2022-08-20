class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        # get the smallest elements, keep track of the row and col
        # (value, row, col)
        heap = [(row[0], i, 0) for i, row in enumerate(nums)] 
        heapify(heap)
        
        result = (-math.inf, math.inf)
        right = max(row[0] for row in nums)
        
        while heap:
            
            left, r, c = heappop(heap)
            
            if right - left < result[1] - result[0]:
                result = (left, right) # found a smaller range
            
            if c + 1 == len(nums[r]):
                return result
            
            nxt = nums[r][c + 1]
            
            right = max(right, nxt) # update right bound if its bigger
            heappush(heap, (nxt, r, c + 1))