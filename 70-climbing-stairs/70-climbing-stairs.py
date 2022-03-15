class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n
        
        # initialize dp array
        dp = [0]* (n+1)
        dp[1] = 1
        dp[2] = 2
        
        i = 3
        while i <= n:
            
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        
        return dp[n]
            