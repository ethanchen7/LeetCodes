class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        maxStartHeap = []
        maxEndHeap = []
        
        n = len(intervals)
        result = [-1] * n
        
        for i in range(n):
            heappush(maxStartHeap, (-intervals[i][0], i))
            heappush(maxEndHeap, (-intervals[i][1], i))

        for _ in range(n):
            topEnd, endIndex = heappop(maxEndHeap)
            if maxStartHeap and maxStartHeap[0][0] <= topEnd:
                topStart, startIndex = heappop(maxStartHeap)
                while maxStartHeap and maxStartHeap[0][0] <= topEnd:
                    topStart, startIndex = heappop(maxStartHeap)
                
                result[endIndex] = startIndex
                heappush(maxStartHeap, (topStart, startIndex))
        
        return result