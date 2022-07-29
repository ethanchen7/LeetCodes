class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1] * (n + 1)
        
        def memo(dp, n):
            
            if n == 0:
                return 0
            
            if n <= 2:
                return 1
            
            if dp[n] != -1: # if we've already encountered this problem, return
                return dp[n]
            
            dp[n] = memo(dp, n - 2) + memo(dp, n-1) # cache the result in dp array
            
            return dp[n] # return the value

        return memo(dp, n)