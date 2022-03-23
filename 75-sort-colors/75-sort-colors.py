class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, i = 0, 0
        high = len(nums) - 1
        
        while i <= high:
            
            # move all the 0s to the low pointer
            # move low and i forward, because we know everything at the low is sorted
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                i += 1
                low += 1
            
            elif nums[i] == 1:
                i += 1
            
            # move all the 2s to the high pointer
            # decrement high but not i, since we still need to check the new i
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
        
        return nums