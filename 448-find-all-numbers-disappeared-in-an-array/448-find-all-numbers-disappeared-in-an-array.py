class Solution(object):
    def findDisappearedNumbers(self, nums):
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
        
        missing_numbers = []
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
        
        return missing_numbers
        
#         for n in nums:
#             idx = abs(n) - 1
#             nums[idx] = -1 * abs(nums[idx])
        
        
#         res = []
#         for i, n in enumerate(nums):
#             if n > 0:
#                 res.append(i + 1)
        
#         return res