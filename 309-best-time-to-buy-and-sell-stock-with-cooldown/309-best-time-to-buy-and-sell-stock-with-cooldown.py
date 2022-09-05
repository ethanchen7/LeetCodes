class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two types of decisions
        # buy or cooldown
        # sell or cooldown
        
        n = len(prices)
        
        memo = {}
        
        def dfs(idx, buying):
            
            if idx >= n:
                return 0
            
            if (idx, buying) in memo:
                return memo[(idx, buying)]
        
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx]
                cooldown = dfs(idx + 1, buying)
                memo[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, not buying) + prices[idx]
                cooldown = dfs(idx + 1, buying)
                memo[(idx, buying)] = max(sell, cooldown)
            
            return memo[(idx, buying)]
        
        return dfs(0, True) 