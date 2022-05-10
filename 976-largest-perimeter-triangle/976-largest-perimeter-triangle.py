class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        # [ 1, 1, 2 ]
        
        max_perim = 0
        
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                max_perim = max(max_perim, nums[i] + nums[i + 1] + nums[i + 2])
        
        return max_perim
        