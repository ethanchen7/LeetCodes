from heapq import *

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num: # insert all the small numbers into maxHeap
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            popped_num = heappop(self.maxHeap)
            heappush(self.minHeap, -popped_num)
            
        elif len(self.minHeap) > len(self.maxHeap):
            popped_num = heappop(self.minHeap)
            heappush(self.maxHeap, -popped_num)
        
        self.length += 1
        
    def findMedian(self) -> float:
        
        if self.length % 2 == 0:
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        else:
            return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()