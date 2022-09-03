class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(remain):
            
            if remain in memo:
                return memo[remain]
            
            if remain == 0:
                return 1
            
            if remain < 0:
                return 0
            
            count = 0
            for i in range(0, len(nums)):
                
                if nums[i] <= remain:
                    count += dfs(remain - nums[i])
            
            memo[remain] = count
            return memo[remain]
        
        return dfs(target)

                
                
                
            