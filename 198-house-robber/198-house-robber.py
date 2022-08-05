class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0]= nums[0]
        
        # two decisions: rob two houses before and this one, or just don't rob this one, rob the previous one
        for i in range(1, len(nums)):
            rob_two_houses_before = dp[i - 2] + nums[i]
            rob_one_house_before = dp[i - 1]
            dp[i] = max(rob_two_houses_before, rob_one_house_before)

        return max(dp)