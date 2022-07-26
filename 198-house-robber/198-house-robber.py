class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: return 0
    
        N = len(nums)
        
        if N <= 2:
            return max(nums)
        
        dp = [0] * N
        dp[0] = nums[0]
        
        i = 1
        
        while i < len(nums):
            
            dp[i] = max(dp[i-1], nums[i] + dp[i-2]) # don't rob this one, or rob this one 
            i += 1
        
        return dp[N - 1]
        