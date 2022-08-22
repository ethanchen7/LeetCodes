class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMin = nums[0]
        currMax = nums[0]
        tempMax = 0
        
        res = max(nums)
        
        for i in range(1, len(nums)):
            
            temp = currMax * nums[i]
            currMax = max(nums[i], currMax * nums[i], currMin * nums[i])
            currMin = min(nums[i], temp, currMin * nums[i])
            
            res = max(res, currMax)
            
        return res