from heapq import *
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
            
        if len(self.maxHeap) > len(self.minHeap) + 1:
            num = -heappop(self.maxHeap)
            heappush(self.minHeap, num)
            
        elif len(self.minHeap) > len(self.maxHeap): # we always want the maxHeap to have more
            num = heappop(self.minHeap)
            heappush(self.maxHeap, -num)
        
        self.length += 1
        
    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()