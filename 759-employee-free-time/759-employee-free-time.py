"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        schedules = []
        for interval in schedule:
            for i in interval:
                schedules.append(i)
                
        schedules.sort(key=lambda x : x.start)
        #[1,2], [1,3], [4,10],[5,6]
        result = []
        
        end_time = schedules[0].end
        for i in range(1, len(schedules)):
            curr_start, curr_end = schedules[i].start, schedules[i].end
            if curr_start > end_time:
                result.append(Interval(end_time, curr_start))
            
            end_time = max(curr_end, end_time)
        
        return result