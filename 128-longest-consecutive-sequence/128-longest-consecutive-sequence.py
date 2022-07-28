class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_length = 0
        
        for num in nums:
            if (num - 1) not in nums_set: # if it's the start of the sequence
                n = num
                length = 0
                while n in nums_set:
                    length += 1
                    n += 1
                max_length = max(length, max_length)
        
        return max_length
                    