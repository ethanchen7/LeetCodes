class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxNum = 0
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            # if the left side of the point is less, and the right side of the point is greater
            # then the point must be a peak
            
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            
            # if the number to the left of mid is greater, and the number to the right less, then we need to move left more
            elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
            