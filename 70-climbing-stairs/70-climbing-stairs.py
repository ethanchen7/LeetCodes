class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [i for i in range(n + 1)]
        
        if n <= 2:
            return dp[n]
        
        i = 3
        while i <= n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i+= 1
        
        return dp[n]