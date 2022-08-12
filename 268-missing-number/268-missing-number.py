class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_set = set(nums)
        
        for i in range(len(nums)):
            if i not in nums_set:
                return i
        
        return len(nums)