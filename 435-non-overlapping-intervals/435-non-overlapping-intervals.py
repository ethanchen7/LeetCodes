class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # first sort by the end point, this guarantees that the ending point is always increasing
        # so we just need to check that the starting point is passed the latest ending point
                # so we'll always want to update the latest ending point
            
        intervals.sort(key=lambda x:x[1])
        
        count = 1 # count of all valid intervals, nonoverlapping
        curr_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= curr_end:
                count += 1
                curr_end = intervals[i][1]
        
        return len(intervals) - count