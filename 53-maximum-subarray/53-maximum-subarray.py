class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum, currentMax = nums[0], 0
        
        for n in nums:
            
            currentMax = max(n, n + currentMax)
            maxSum = max(maxSum, currentMax)
        
        return maxSum
            