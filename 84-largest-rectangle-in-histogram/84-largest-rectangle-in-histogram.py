class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        if n < 2:
            return heights[0]
        
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            curr_idx = i
            while stack and stack[-1][0] > h:
                prev_height, prev_idx = stack.pop()
                curr_idx = prev_idx
                max_area = max(prev_height * (i - prev_idx), max_area)
            
            stack.append([h, curr_idx])
        
        while stack:
            height, idx = stack.pop()
            max_area = max(max_area, ((n-1) - idx + 1) * height)
        
        return max_area