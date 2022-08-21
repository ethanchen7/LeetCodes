class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height = 0
        
        left, right = 0, len(height) - 1
        
        while left < right:
            
            _height = min(height[left], height[right]) * (right - left)
            
            max_height = max(_height, max_height)
            
            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        
        return max_height