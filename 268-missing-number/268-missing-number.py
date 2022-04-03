class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        while i < len(nums):
            
            j = nums[i] # the correct index position
            
            # check for outer bound because we can't swap when index is out of range
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            
            else:
                i += 1
        
        
        for n in range(len(nums)):
            if nums[n] != n:
                return n
        
        return len(nums)