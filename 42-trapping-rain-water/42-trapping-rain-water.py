class Solution:
    def trap(self, height: List[int]) -> int:
        
        totalWater = 0
        n = len(height)
        
        leftMaxes = [0] * n
        rightMaxes = [0] * n
        
        leftMax = 0
        for i in range(n):
            leftMax = max(leftMax, height[i])
            leftMaxes[i] = leftMax
        
        rightMax = 0
        for j in range(n - 1, -1, -1):
            rightMax = max(rightMax, height[j])
            rightMaxes[j] = rightMax
        
        for i, h in enumerate(height):
            
            minHeight = min(leftMaxes[i], rightMaxes[i])
            water = minHeight - h
            totalWater += water
        
        return totalWater