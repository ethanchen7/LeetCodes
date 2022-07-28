class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = nums[:] + [0]
        
        if len(nums) <= 2:
            return max(nums)
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        print(dp)
        return dp[len(nums) - 1]