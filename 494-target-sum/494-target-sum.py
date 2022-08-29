class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.memo = {}
        
        def dfs(idx, total):
            
            key = (idx, total)
            
            if key in self.memo:
                return self.memo[key]
            
            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if idx > len(nums):
                return 0
            
            add = dfs(idx + 1, total + nums[idx])
            subtract = dfs(idx + 1, total - nums[idx])
            
            self.memo[key] = add + subtract
            return self.memo[key]
        
        return dfs(0, 0)