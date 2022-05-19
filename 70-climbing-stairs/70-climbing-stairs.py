class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 2
        
        
        if n > 2:
            i = 3
            while i <= n:
                dp[i] = dp[i - 2] + dp[i - 1]
                i += 1
        
        return dp[n]
            
            
        