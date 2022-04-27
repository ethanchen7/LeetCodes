class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.result = []
        nums.sort()
        # [-2, -1, 0, 0, 1, 2]
        
        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                
                self.search(target, nums, a, b, b + 1)
        
        return self.result
    
    def search(self, target, nums, a, b, low):
        
        high = len(nums) - 1
        
        while low < high:
            
            current_sum = nums[a] + nums[b] + nums[low] + nums[high]
            
            if current_sum == target:
                self.result.append([nums[a], nums[b], nums[low], nums[high]])
                
                low += 1
                high -= 1
                
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            
            if current_sum < target:
                low += 1
            
            if current_sum > target:
                high -= 1
        
            