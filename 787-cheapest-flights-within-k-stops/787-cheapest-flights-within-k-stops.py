class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # for k + 1 times
            # go through all the flights, find the new prices to reach each destination node
        
        prices = [math.inf for i in range(n)]
        prices[src] = 0
        
        for i in range(k + 1):
            
            tmpPrices = prices[:]
            
            for s, d, c in flights:
                
                if prices[s] == math.inf:
                    continue
                
                if prices[s] + c < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + c
            print(prices, 'prices')
            print(tmpPrices, 'tmpPrices')
            prices = tmpPrices
            
        
        return prices[dst] if prices[dst] != math.inf else -1