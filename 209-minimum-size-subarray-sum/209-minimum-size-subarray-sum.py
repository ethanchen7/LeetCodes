import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len = math.inf
        curr_sum, start = 0, 0
        
        for end in range(0, len(nums)):
            
            curr_sum += nums[end]
            
            while curr_sum >= target:
                min_len = min(min_len, (end - start + 1))
                curr_sum -= nums[start]
                start += 1
        
        if min_len == math.inf:
            return 0
        
        return min_len