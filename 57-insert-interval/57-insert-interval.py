class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        result = []
        
        for i, interval in enumerate(intervals):
            
            if interval[0] > newInterval[1]:
                result.append(newInterval)
                result += intervals[i:]
                return result
                
            elif interval[0] <= newInterval[1] and interval[1] >= newInterval[0]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            
            else:
                result.append(interval)
        
        result.append(newInterval)
        return result