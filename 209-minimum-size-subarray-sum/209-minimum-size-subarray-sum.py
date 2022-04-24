class Solution(object):
    
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        min_len = 99999
        start, curr_sum = 0, 0
        
        for end in range(len(nums)):
            right = nums[end]
            
            curr_sum += right
            
            while curr_sum >= target:
                
                curr_len = end - start + 1
                min_len = min(curr_len, min_len)
                
                left = nums[start]
                curr_sum -= left
                start += 1
        
        if min_len == 99999:
            return 0
        return min_len