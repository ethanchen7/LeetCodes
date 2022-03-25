class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while (low < len(nums) - 1 and nums[low] <= nums[low + 1]):
            low += 1
        
        if low == len(nums) - 1:
            return 0
    
        while (high > 0 and nums[high] >= nums[high - 1]):
            high -= 1
        
        subarr_max = -math.inf
        subarr_min = math.inf
        
        for i in range(low, high + 1):
            subarr_max = max(subarr_max, nums[i])
            subarr_min = min(subarr_min, nums[i])
        
        while (low > 0 and nums[low - 1] > subarr_min):
            low -= 1
        
        while (high < len(nums) - 1 and nums[high + 1] < subarr_max):
            high += 1
        
        return high - low + 1