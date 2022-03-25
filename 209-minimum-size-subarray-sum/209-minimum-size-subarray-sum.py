class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        curr_sum = 0
        min_len = 999999
        for end in range(len(nums)):
            curr_sum += nums[end]
            
            while curr_sum >= target:
                min_len = min(end - start + 1, min_len)
                curr_sum -= nums[start]
                start += 1
        
        if min_len == 999999:
            return 0
        return min_len