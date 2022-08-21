class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low, high = 0, len(nums) - 1
        pointer = 0
        
        while pointer <= high:
            
            if nums[pointer] == 0:
                nums[pointer], nums[low] = nums[low], nums[pointer]
                low += 1
                pointer = low
            
            elif nums[pointer] == 1:
                pointer += 1
            
            elif nums[pointer] == 2:
                nums[pointer], nums[high] = nums[high], nums[pointer]
                high -= 1
            
            
            