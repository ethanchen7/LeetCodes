class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        
        if len(nums) == 1:
            return 0
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if mid > 0 and mid < len(nums) - 1:
                if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                    return mid
                
                elif nums[mid - 1] < nums[mid] < nums[mid + 1]: # check if we're on a slope
                    left = mid + 1  # keep going on the slope
            
                else:
                    right = mid - 1
            
            elif mid == 0 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return left