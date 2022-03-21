class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = [0 for x in nums]
        left = 0
        n = len(nums) - 1
        right, largest_num_idx = n, n
        
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            
            if left_square < right_square:
                squares[largest_num_idx] = right_square
                right -= 1
            
            else:
                squares[largest_num_idx] = left_square
                left += 1
            
            largest_num_idx -= 1
        
        return squares
        