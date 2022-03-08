class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        minProd = 1
        maxProd = 1
        
        for n in nums:
            if n == 0:
                minProd = 1
                maxProd = 1
            
            temp = n * maxProd
            maxProd = max(n, n*maxProd, n*minProd)
            minProd = min(n, temp, n*minProd)
            
            res = max(res, maxProd)
        
        return res