class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key=lambda x:x[1])
        # [[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]
        
        max_time_heap = []
        
        time = 0
        count = 0
        for cost, deadline in courses:
            time += cost
            heappush(max_time_heap, -cost)
            count += 1
            
            if time > deadline:
                time += heappop(max_time_heap)
                count -= 1
        
        return count