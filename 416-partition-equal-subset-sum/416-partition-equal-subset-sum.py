class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if (sum(nums) % 2 != 0):
            return False
        
        target = sum(nums) // 2
        
        dp = [[False for i in range(target + 1)] for j in range(len(nums))]
        
        for i in range(target + 1):
            if nums[0] == i:
                dp[0][i] = True
        
        for j in range(len(nums)):
            dp[j][0] = True
        
        for i in range(1, len(nums)):
            for t in range(1, target + 1):
                if dp[i - 1][t]:
                    dp[i][t] = dp[i - 1][t]
                
                elif t >= nums[i]:
                    dp[i][t] = dp[i - 1][t] or dp[i - 1][t - nums[i]]
        
        return dp[-1][target]