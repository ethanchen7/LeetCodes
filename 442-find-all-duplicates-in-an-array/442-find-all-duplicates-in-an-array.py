class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []
        
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        
        return result