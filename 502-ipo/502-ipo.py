class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # throw all the capital into a minHeap
        # throw all the projects you can afford into a maxHeap, pick the first K elements
        
        minCapitalHeap = []
        maxProfitHeap = []
        
        for i in range(len(capital)):
            heappush(minCapitalHeap, [capital[i], i])
        
        availableCapital = w
        
        for _ in range(k):
            
            while minCapitalHeap and availableCapital >= minCapitalHeap[0][0]:
                capital, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, -profits[i])
            
            if not maxProfitHeap:
                break
                
            availableCapital += -heappop(maxProfitHeap)
        
        return availableCapital