class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(1, len(prices)):
            
            if prices[i] < minPrice:
                minPrice = prices[i]
                
            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit
            