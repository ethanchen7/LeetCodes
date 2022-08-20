"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        # flatten the intervals into one sorted list
        # just find the gaps between the intervals
        
        schedules = []
        for s in schedule:
            for i in s:
                schedules.append(i)
                
        schedules.sort(key=lambda x : x.start)
        # [1,2], [1,3], [4,10], [5,6]
        res = []
        
        end = schedules[0].end
        for interval in schedules[1:]:
            
            if interval.start > end:
                res.append(Interval(end, interval.start))
            
            end = max(end, interval.end)
        
        return res