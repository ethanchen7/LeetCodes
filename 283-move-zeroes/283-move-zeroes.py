class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_idx = 0
        
        for pointer in range(len(nums)):
            if nums[pointer] != 0:
                nums[zero_idx], nums[pointer] = nums[pointer], nums[zero_idx]
                zero_idx += 1
            pointer += 1