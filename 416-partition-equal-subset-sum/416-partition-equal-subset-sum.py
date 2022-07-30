class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if (sum(nums) % 2) != 0:
            return False
        
        target = sum(nums) // 2
        
        dp = [[-1 for i in range(target + 1)] for x in range(len(nums))]
        
        def dfs(idx, total):
            
            if total == target:
                return True
            
            if total > target or idx >= len(nums):
                return False
            
            if dp[idx][total] != -1:
                return dp[idx][total]
            
            total1 = dfs(idx + 1, total + nums[idx])
            total2 = dfs(idx + 1, total)
            
            dp[idx][total] = (total1 or total2)
            
            return dp[idx][total]
        
        return dfs(0, 0)