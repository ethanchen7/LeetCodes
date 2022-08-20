class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # sort the intervals by start time
        # use a stack and a heap
        
        # heapify the intervals
        # push ongoing meetings on to the stack
        # return len of stack
        
        heapify(intervals)
        times = []
        
        while intervals:
            
            s, e = heappop(intervals)
            if times and times[0] <= s:
                heappop(times)
            heappush(times, e)
            
        
        return len(times)