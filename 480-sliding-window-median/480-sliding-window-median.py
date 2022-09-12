class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        n = len(nums)
        res = []
        
        # store all the bigger numbers in minheap, smaller in maxHeap
        # ex: [1,2,3,4,5,6] window
        # minHeap = [4,6,5]
        # maxHeap = [-3,-1,-2]
        
        minHeap = [] 
        maxHeap = []
        
        def getMedian():
            if not minHeap and not maxHeap:
                return 0
            if len(minHeap) != len(maxHeap): # odd
                return minHeap[0]
            else: 
                return (minHeap[0] - maxHeap[0]) / 2 # even
        
        def balanceHeaps():
            
            if len(minHeap) < len(maxHeap):
                num = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, num)
            
            if (len(minHeap) - len(maxHeap)) > 1:
                num = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -num)
            
        def insert(num):
            
            median = getMedian()
            if num >= median:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappush(maxHeap, -num)
            balanceHeaps()
        
        def remove(num):
            
            median = getMedian()
            if num >= median: # it's in the maxHeap
                minHeap.remove(num)
                heapq.heapify(minHeap)
            
            else:
                maxHeap.remove(-num)
                heapq.heapify(maxHeap)
            balanceHeaps()
        
        for i in range(n):
            
            insert(nums[i])
            
            if i >= k: # maintain window size
                num = nums[i - k]
                remove(num)
            
            if i >= k - 1:
                res.append(getMedian())
        
        return res
            