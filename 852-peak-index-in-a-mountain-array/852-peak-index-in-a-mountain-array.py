class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
            
            else:
                left = mid + 1
    
                