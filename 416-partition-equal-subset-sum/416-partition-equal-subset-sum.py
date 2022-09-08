class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target_sum = s // 2
        
        dp = [[False] * (target_sum + 1) for _ in range(len(nums))]
        
        for t in range(0, target_sum + 1):
            dp[0][t] = nums[0] == t
        
        for i in range(len(nums)):
            dp[i][0] = True
            
        for t in range(1, target_sum + 1):
            for i in range(1, len(nums)):
                if t >= nums[i]:
                    dp[i][t] = dp[i - 1][t - nums[i]] or dp[i - 1][t]
                else:
                    dp[i][t] = dp[i - 1][t]

        return dp[len(nums) - 1][target_sum]