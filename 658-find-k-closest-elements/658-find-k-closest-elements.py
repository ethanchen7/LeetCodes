class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        index = self.binary_search(arr, x)
        low = max(index - k, 0)
        high = min(index + k, len(arr) - 1) 
        
        for i in range(low, high + 1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))
        
        res = []
        for _ in range(k):
            res.append(heappop(minHeap)[1])
        
        res.sort()
        return res
    
    def binary_search(self, arr, x):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            if arr[mid] == x: 
                return mid
            
            if arr[mid] < x:
                left = mid + 1
            
            if arr[mid] > x:
                right = mid - 1
        
        return left