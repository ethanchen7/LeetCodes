class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            # get rid of duplicates
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] < nums[right]: # right side is sorted, check that our target is in there
                
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            else: # left side is sorted, check that our target is in there
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False