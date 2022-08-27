class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key=lambda x:x[1])
        
        maxHeap = []
        max_time = 0
        
        for time, end_time in courses:
            heappush(maxHeap, -time)
            max_time += time
            
            if max_time > end_time:
                biggest_time = -heappop(maxHeap)
                max_time -= biggest_time
        
        return len(maxHeap)