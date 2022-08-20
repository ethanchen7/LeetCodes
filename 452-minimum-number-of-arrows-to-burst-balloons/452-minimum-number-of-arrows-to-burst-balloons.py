class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # we sort by the end coordinate, which GUARANTEES that 
        # the next balloons all end at the SAME time or AFTER it
        # the only thing we care about then is that the next balloon starts AFTER the current balloon
        # if that's the case, we will need another arrow
        
        points.sort(key=lambda x: x[1]) 
        
        stack = [points[0][1]]
        
        for start, end in points[1:]:
            
            if stack and stack[-1] < start: # if the previous balloon ended already
                stack.append(end)
            else:
                continue
        
        return len(stack)