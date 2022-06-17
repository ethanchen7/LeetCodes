class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = nums[0]
        current_sum = 0
        
        for n in nums:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)
        
        return max_sum