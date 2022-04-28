class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        
        result = []
        # [[3,5], [6,7], [8,10]]      [4,8]
        # [[6,7], [8,10]]             [3,8]
        for i in range(len(intervals)):
            
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            elif newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            
            else:
                result.append(intervals[i])
        
        result.append(newInterval)
        return result