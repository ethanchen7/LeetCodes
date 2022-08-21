class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        count = 0
        window_start = 0
        total = 1
    
        for window_end in range(len(nums)):
            total *= nums[window_end]
            
            while total >= k:
                total /= nums[window_start]
                window_start += 1
            
            count += window_end - window_start + 1
           
        return count