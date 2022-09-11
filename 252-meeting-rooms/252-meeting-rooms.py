class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        
        latest_end = 0
        
        for start, end in intervals:
            if start < latest_end:
                return False
            latest_end = end
        
        return True