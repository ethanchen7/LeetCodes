import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_k = max(piles)
        min_speed = max(piles)
        
        left = 1
        right = max_k
        
        while left <= right:
            
            mid_k = left + (right - left) // 2
            hours = 0
            
            for p in piles:
                time = math.ceil(p / mid_k)
                hours += time
        
            if hours <= h:
                min_speed = min(min_speed, mid_k)
                right = mid_k - 1
            
            else:
                left = mid_k + 1
        
        return min_speed