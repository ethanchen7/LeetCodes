class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        count = 0
        
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    count += right - left # we already know all the numbers to the left of right will result in sum < target
                    left += 1
                else:
                    right -= 1
        
        return count