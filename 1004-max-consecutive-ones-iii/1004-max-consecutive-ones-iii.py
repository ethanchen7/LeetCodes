class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_len = 0
        start = 0
        ones_frequency = 0
        
        for end in range(len(nums)):
            
            if nums[end] == 1:
                ones_frequency += 1
            
            if (end - start + 1 - ones_frequency > k):
                left = nums[start]
                if left == 1: 
                    ones_frequency -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len