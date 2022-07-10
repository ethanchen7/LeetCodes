class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # cyclic sort the array
        i = 0
        while i < len(nums):
            j = nums[i]
            if j < len(nums) - 1 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)
                
            