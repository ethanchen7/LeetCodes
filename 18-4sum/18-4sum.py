class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        quadruplets = []
        for i in range(0, len(nums)-3):
        # skip same element to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)-2):
            # skip same element to avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.search_pairs(nums, target, i, j, quadruplets)
        return quadruplets


    def search_pairs(self, nums, target_sum, first, second, quadruplets):
        left = second + 1
        right = len(nums) - 1
        while (left < right):
            quad_sum = nums[first] + nums[second] + nums[left] + nums[right]
            
            if quad_sum == target_sum:  # found the quadruplet
                quadruplets.append(
                [nums[first], nums[second], nums[left], nums[right]])
                left += 1
                right -= 1
                while (left < right and nums[left] == nums[left - 1]):
                    left += 1  # skip same element to avoid duplicate quadruplets
                while (left < right and nums[right] == nums[right + 1]):
                    right -= 1  # skip same element to avoid duplicate quadruplets
                    
            elif quad_sum < target_sum:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum
                

        