class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        maxProd, minProd = 1, 1
        
        for n in nums:
            
            if n == 0:
                maxProd = 1
                minProd = 1
                
            temp_max = maxProd * n
            maxProd = max(n, n*maxProd, n*minProd)
            minProd = min(n, temp_max, n*minProd)
            
            res = max(res, maxProd)
        
        return res