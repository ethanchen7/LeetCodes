class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        num_idx = self.binary_search(nums, target)
        if num_idx == -1:
            return [-1, -1]
        
        start, end = num_idx, num_idx
        while start > 0 and nums[start - 1] == nums[num_idx]:
            start -= 1
        
        while end < len(nums) - 1 and nums[end + 1] == nums[num_idx]:
            end += 1
        
        return [start, end]
    
    def binary_search(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
        
            if nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1