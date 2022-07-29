class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[left] <= nums[mid]: # left side is sorted
                if nums[right] < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if nums[right] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
    
                
            
            