class Solution:
    import math
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest_sum = 0
        min_difference = math.inf
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                
                current_sum = nums[i] + nums[low] + nums[high]
                current_diff = abs(target -current_sum) # absolute difference between the two values
                
                if current_diff < min_difference:
                    closest_sum = current_sum
                    min_difference = current_diff
                
                if current_sum < target:
                    low += 1
                
                elif current_sum > target:
                    high -= 1
                    
                else:
                    return current_sum
        
        return closest_sum