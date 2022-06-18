class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.reverse()
        K = k % len(nums)
        
        if len(nums) < 2:
            return
        
        left = 0
        right = K - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        left2 = K
        right2 = len(nums) - 1
        
        while left2 < right2:
            nums[left2], nums[right2] = nums[right2], nums[left2]
            left2 += 1
            right2 -= 1
        
        return nums
        