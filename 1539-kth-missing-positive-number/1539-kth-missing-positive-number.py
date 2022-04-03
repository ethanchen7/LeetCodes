class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        j = 1
        for i in range(0, len(arr)):
            
            while arr[i] != j:
                k -= 1
                
                if k == 0:
                    return j
                
                j += 1
            
            j += 1
        
        while k > 1:
            j += 1
            k -= 1
        
        return j