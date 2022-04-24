class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums_len = len(nums)
        expected_sum = 0
        for n in range(nums_len + 1):
            expected_sum += n
        
        actual_sum = 0
        for i in nums:
            actual_sum += i
        
        return expected_sum - actual_sum