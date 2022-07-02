class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squares = [0] * len(nums)
        top_idx = len(nums) - 1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            
            if left_sq >= right_sq:
                squares[top_idx] = left_sq
                left += 1
            
            else:
                squares[top_idx] = right_sq
                right -= 1
            
            top_idx -= 1
        
        return squares
        
        