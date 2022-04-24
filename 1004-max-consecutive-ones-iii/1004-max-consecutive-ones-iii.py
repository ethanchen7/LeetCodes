class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # one_frequency = {}
        start, max_len = 0, 0
        
        for end in range(len(nums)):
            right = nums[end]
            if right == 0:
                k -= 1
            
            if k < 0:
                left = nums[start]
                if left == 0:
                    k += 1
                start += 1
                
            curr_len = end - start + 1
            max_len = max(max_len, curr_len)
        
        return max_len
            