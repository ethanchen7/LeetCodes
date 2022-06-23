from heapq import *
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        mins = nsmallest(2, nums)
        maxs = nlargest(3, nums)
        
        # we could have a largest number in the minimum product (because of negatives)
        # take the two smallest (most negative) and largest number
        min_prod = mins[0] * mins[1] * maxs[0]
        
        max_prod = maxs[0] * maxs[1] * maxs[2]
        
        return max(min_prod, max_prod)