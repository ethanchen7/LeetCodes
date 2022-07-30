class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = [[-math.inf for i in range(-(sum(nums) + 1), sum(nums) + 1)] for x in range(len(nums))]
        
        def dfs(idx, total):
            
            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            else:
                
                if memo[idx][total] != -math.inf:
                    return memo[idx][total]
                
                sum1 = dfs(idx + 1, total + nums[idx])
                sum2 = dfs(idx + 1, total - nums[idx])
                
                memo[idx][total] = sum1 + sum2
                return memo[idx][total]
        
        return dfs(0, 0)