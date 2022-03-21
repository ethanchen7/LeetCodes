
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        smallest_difference = 9999999
        
        for i in range(len(nums) - 2):
            
            right = len(nums) - 1
            left = i + 1
            
            while left < right:
                current_diff = target - nums[i] - nums[left] - nums[right]
                if current_diff == 0:
                    return target
                
                if abs(current_diff) < abs(smallest_difference) or (abs(current_diff) == abs(smallest_difference) and current_diff > smallest_difference):
                    smallest_difference = current_diff
                
                if current_diff > 0:
                    left += 1
                else:
                    right -= 1
        
        return target - smallest_difference