class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start, end = 0, len(nums) - 1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]: # check if left side is sorted
                if target >= nums[start] and target < nums[mid]: # if it's in that range
                    end = mid - 1 # adjust bounds
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1