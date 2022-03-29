class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        for i in range(len(intervals)):
            
            # if the end of the new interval is before the start of the first interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # if the interval is passed the interval we're currently checking
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res