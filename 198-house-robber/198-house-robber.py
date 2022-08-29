class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        
        for i in range(2, len(dp)):
            dont_rob = dp[i - 1]
            rob = dp[i - 2] + nums[i - 1]
            
            dp[i] = max(dont_rob, rob)
        
        return dp[-1]
        