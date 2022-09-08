class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [math.inf for i in range(amount + 1)]
        dp[0] = 0
        
        for amt in range(amount + 1):
            for c in coins:
                if amt >= c:
                    dp[amt] = min(dp[amt], dp[amt - c] + 1)
        
        return dp[amount] if dp[amount] != math.inf else -1