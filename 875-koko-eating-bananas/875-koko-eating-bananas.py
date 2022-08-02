import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        minimum_k = right
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                minimum_k = min(minimum_k, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return minimum_k