class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        left = 0
        product = 1
        
        if k <= 1:
            return 0
        
        for right in range(len(nums)):
            product *= nums[right]
            while (product >= k and left < len(nums)):
                product /= nums[left]
                left += 1
            
            result += right - left + 1
        
        return result