class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        expected_sum = 0
        for i in range(n + 1):
            expected_sum += i
        
        current_sum = 0
        for n in nums:
            current_sum += n
        
        return expected_sum - current_sum