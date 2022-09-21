class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            
            next_interval = intervals[i]
            if result[-1][1] < next_interval[0]:
                result.append(next_interval)
            
            else:
                result[-1][0] = min(next_interval[0], result[-1][0])
                result[-1][1] = max(next_interval[1], result[-1][1])
        
        return result