class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * (len(cost) + 1) # + 1 because we need the last floor as the final step to reach
        
        for i in range(2, len(cost) + 1):
            
            one_step = dp[i - 1] + cost[i - 1]
            two_step = dp[i - 2] + cost[i - 2]
            dp[i] = min(one_step, two_step)
        
        return dp[-1]
        