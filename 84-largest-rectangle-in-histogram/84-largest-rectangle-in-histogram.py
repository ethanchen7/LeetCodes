class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        if n < 2:
            return heights[0]
        
        stack = []
        max_area = 0
        for i in range(n):
            curr_height = heights[i]
            curr_idx = i
            while stack and stack[-1][0] > curr_height:
                prev_height, prev_idx = stack.pop()
                curr_idx = prev_idx
                width = i - prev_idx
                area = width * prev_height
                max_area = max(area, max_area)
            
            stack.append([curr_height, curr_idx])
        
        while stack:
            height, idx = stack.pop()
            area = ((n-1) - idx + 1) * height
            max_area = max(max_area, area)
        
        return max_area