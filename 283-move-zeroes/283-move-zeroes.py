class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = 0
        
        for pointer in range(len(nums)):
            if nums[pointer] != 0:
                nums[zero], nums[pointer] = nums[pointer], nums[zero]
                zero += 1
            
            pointer += 1
        
        