class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        duplicates = set()
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.add(nums[i])
        
        return duplicates