class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        
        nums.sort()
        
        memo = {}
        def dfs(idx, total):
            
            key = (idx, total)
            
            if key in memo:
                return memo[key]
            
            if total == 0:
                return True
            
            if idx >= len(nums) or total < 0:
                return False
            
            take = dfs(idx + 1, total - nums[idx])
            dont_take = dfs(idx + 1, total)
            
            memo[key] = take or dont_take
            return memo[key]
        
        return dfs(0, target)