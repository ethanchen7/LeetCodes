class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float('inf')
        max_profit = 0
        
        for n in prices:
            
            if n < min_price:
                min_price = n
            
            profit = n - min_price
            max_profit = max(profit, max_profit)
        
        return max_profit