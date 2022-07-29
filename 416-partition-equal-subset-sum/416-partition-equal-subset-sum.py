class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        
        s = sum(nums) // 2
        
        dp = [[-1 for x in range(s + 1)] for i in range(len(nums))]
        
        def dfs(total, i):
            
            if total > s or i >= len(nums):
                return False
            
            if total == s:
                return True
            
            if dp[i][total] != -1:
                return dp[i][total]
        
            result1 = dfs(total + nums[i], i + 1)
            result2 = dfs(total, i + 1)
            
            dp[i][total] = result1 or result2
            return dp[i][total]
        
        return dfs(0, 0)
        
        