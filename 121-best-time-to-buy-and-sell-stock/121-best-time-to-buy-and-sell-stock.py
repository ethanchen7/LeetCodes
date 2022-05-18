class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = 9999
        maxProfit = 0
        
        for num in prices:
            minPrice = min(num, minPrice)
            
            maxProfit = max(maxProfit, num - minPrice)
        
        return maxProfit
        