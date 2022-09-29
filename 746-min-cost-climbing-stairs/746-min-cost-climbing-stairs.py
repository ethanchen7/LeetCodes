class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0
        
        for i in range(2, len(cost) + 1):
            jumpTwo = dp[i - 2] + cost[i - 2]
            jumpOne = dp[i - 1] + cost[i - 1]
            
            dp[i] = min(jumpTwo, jumpOne)
        
        return dp[-1]