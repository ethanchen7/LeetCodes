class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        
        start, max_len, max_ones_repeat = 0, 0, 0
        
        for end in range(len(nums)):
            right = nums[end]
            if right == 1:
                max_ones_repeat += 1
            
            if (end - start + 1 - max_ones_repeat) > k:
                if nums[start] == 1:
                    max_ones_repeat -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len