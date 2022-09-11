class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        
        intervals.sort()
        # [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            start, end = result[-1]
            current_start, current_end = intervals[i]
            
            if current_start <= end:
                result[-1][0], result[-1][1] = min(start, current_start), max(end, current_end)
            
            else:
                result.append(intervals[i])
        
        return result