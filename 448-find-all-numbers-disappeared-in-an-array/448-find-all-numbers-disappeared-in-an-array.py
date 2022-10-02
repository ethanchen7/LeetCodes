class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            
            else:
                i += 1
        
        result = []
        for n in range(len(nums)):
            if nums[n] != n + 1:
                result.append(n + 1)
        
        return result