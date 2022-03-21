class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: #continue moving the target_sum forward until no dup
                continue 
            self.search(triplets, nums, -nums[i], i + 1)
        return triplets
    
    def search(self, triplets, nums, target_sum, left):
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                
                # keep moving left and right if there are duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1